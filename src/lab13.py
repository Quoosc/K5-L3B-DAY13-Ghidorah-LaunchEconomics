"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Phần A, B đã hoàn thiện; phần D1 và E1 có sẵn hàm tính để đối chiếu.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong (0, 1]')
    if k is None:
        return 1 / p
    if k < 1:
        raise ValueError('k phải lớn hơn hoặc bằng 1')
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong (0, 1]')
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError('k phải lớn hơn hoặc bằng 1')
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong,
    cps (chi phí mỗi việc thành công), hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - chay_lai: token + tool của các lần chạy thứ 2 trở đi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP,
      phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - hoa_don_moi_yc: token + tool chia cho số yêu cầu trong phạm vi.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn
      số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:
        if max_lan_chay < 1:
            raise ValueError('max_lan_chay phải lớn hơn hoặc bằng 1')
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool

    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    if thanh_cong == 0:
        raise ZeroDivisionError('Không có yêu cầu thành công trong phạm vi đã chọn')

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def _in_a2(ket_qua):
    """In bảng A2 đủ 9 dòng để chép vào bang_chi_phi.md."""
    nhan = [
        ('token', 'Token (mọi lần chạy)'),
        ('tool', 'Tool'),
        ('chay_lai', 'Trong đó: lần chạy thứ 2 và 3'),
        ('xem_lai', 'Xem lại [simulated]'),
        ('lam_lai', 'Làm lại [simulated]'),
        ('tong', 'Tổng chi phí (có phần simulated)'),
        ('thanh_cong', 'Số việc thành công'),
        ('cps', 'Chi phí mỗi việc thành công [simulated]'),
        ('hoa_don_moi_yc', 'Hoá đơn token + tool / số yêu cầu'),
    ]
    print('\nA2 · Mô hình chi phí từ trace')
    for khoa, ten in nhan:
        gia_tri = ket_qua[khoa]
        if khoa == 'thanh_cong':
            print(f'{ten:42s} {gia_tri:>14,.0f}')
        else:
            print(f'{ten:42s} {gia_tri:>14,.1f}')
    print(f'{"CPS / hoá đơn mỗi yêu cầu":42s} '
          f'{ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:>14,.2f} lần')


def _in_a3(runs, reqs):
    """In bảng A3 theo loại yêu cầu và tỉ lệ run ok theo lần thử."""
    print('\nA3 · Tách theo loại yêu cầu')
    print(f'{"Loại":10s} {"Số YC":>7s} {"Thành công":>11s} '
          f'{"Lần chạy/YC":>12s} {"CPS [sim]":>13s} {"So 12.000":>10s}')
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        nhom = reqs[reqs['loai'] == loai]
        ket_qua = mo_hinh(runs, nhom)
        ti_le = ket_qua['thanh_cong'] / len(nhom)
        so_lan = nhom['so_lan_chay'].mean()
        print(f'{loai:10s} {len(nhom):>7,d} {ti_le:>10.1%} {so_lan:>12.2f} '
              f'{ket_qua["cps"]:>13,.0f} {ket_qua["cps"] / BASELINE:>9.2f}x')

    print('\nTỉ lệ run ok theo lần thử (trả lời "chạy lại có giúp không")')
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id', how='inner')
    runs_loai['ok'] = (runs_loai['status'] == 'ok').astype(int)
    bang = runs_loai.pivot_table(index='loai', columns='attempt', values='ok',
                                 aggfunc='mean')
    print(f'{"Loại":10s} {"Lần 1":>8s} {"Lần 2":>8s} {"Lần 3":>8s}')
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        if loai in bang.index:
            gia_tri = [bang.loc[loai].get(lan, float('nan')) for lan in (1, 2, 3)]
            print(f'{loai:10s} ' + ' '.join(f'{x:>7.1%}' for x in gia_tri))


def _in_a4(runs, reqs):
    """In bảng A4: cộng chi phí cố định 40 triệu đ/tháng cho phạm vi pilot."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ket_qua = mo_hinh(runs, pham_vi)
    thanh_cong_thang = 45000 * ket_qua['thanh_cong'] / len(reqs)
    cps_truoc_co_dinh = ket_qua['cps']

    print('\nA4 · Chi phí cố định (noi_dia + hang_nang)')
    print(f'{"Khối lượng":24s} {"Việc TC/tháng":>15s} {"Cố định/việc":>14s} '
          f'{"CPS + cố định":>15s} {"So 12.000":>10s}')
    for ten, he_so in (('45.000 yêu cầu/tháng', 1.0), ('Một nửa khối lượng', 0.5)):
        thanh_cong = thanh_cong_thang * he_so
        co_dinh_moi_viec = 40000000 / thanh_cong
        cps = cps_truoc_co_dinh + co_dinh_moi_viec
        print(f'{ten:24s} {thanh_cong:>15,.0f} {co_dinh_moi_viec:>13,.0f} '
              f'{cps:>15,.0f} {cps / BASELINE:>9.2f}x')

    nguong_viec = 40000000 / (BASELINE - cps_truoc_co_dinh)
    nguong_yeu_cau = nguong_viec * len(reqs) / ket_qua['thanh_cong']
    print(f'CPS phạm vi trước cố định: {cps_truoc_co_dinh:,.0f} đ; '
          f'hòa vốn ở khoảng {nguong_viec:,.0f} việc thành công/tháng '
          f'(~{nguong_yeu_cau:,.0f} yêu cầu/tháng).')


def _in_b1_b2(runs, reqs):
    """In bảng độ nhạy B1 và kịch bản cặp B2."""
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = [
        ('Giá token gấp đôi', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', dict(luong_phut=2500)),
        ('Tối đa 2 lần chạy', dict(max_lan_chay=2)),
        ('Chỉ 1 lần chạy', dict(max_lan_chay=1)),
    ]

    print('\nB1 · Đổi từng yếu tố')
    print(f'{"Kịch bản":30s} {"CPS [sim]":>13s} {"Thay đổi":>10s}')
    print(f'{"Gốc (A2)":30s} {goc:>13,.0f} {"":>10s}')
    for ten, tham_so in kich_ban:
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten:30s} {cps:>13,.0f} {(cps / goc - 1) * 100:>+9.1f}%')

    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Giá token gấp đôi + xem lại gấp đôi: {cap:,.0f} đ '
          f'({(cap / goc - 1) * 100:+.1f}%)')
    print('Xếp hạng: 1. số ca làm lại; 2. tỉ lệ xem lại; 3. lương nhân viên')


def _in_b3(runs, reqs):
    """In bảng B3: chi phí cả hệ thống khi giới hạn 1, 2, 3 lần chạy."""
    print('\nB3 · Giới hạn chạy lại có thật sự rẻ hơn')
    print(f'{"Giới hạn":10s} {"Tổng trợ lý [sim]":>19s} {"Không TC":>9s} '
          f'{"Cả hệ thống":>15s} {"CPS [sim]":>12s}')
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        ca_he_thong = ket_qua['tong'] + BASELINE * khong_thanh_cong
        print(f'{gioi_han:>10d} {ket_qua["tong"]:>19,.0f} {khong_thanh_cong:>9,d} '
              f'{ca_he_thong:>15,.0f} {ket_qua["cps"]:>12,.0f}')


def _in_b4(runs, reqs):
    """In kết quả B4: xem lại 100% cho phạm vi noi_dia + hang_nang."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pham_vi = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_yeu_cau_co_ok = runs_pham_vi.loc[
        runs_pham_vi['status'] == 'ok', 'request_id'].nunique()
    so_ca_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    tien_token_tool = (
        runs_pham_vi['tokens_in'] / 1000 * GIA_VAO
        + runs_pham_vi['tokens_out'] / 1000 * GIA_RA
        + runs_pham_vi['tool_calls'] * GIA_TOOL
    ).sum()

    print('\nB4 · Nếu phải xem lại tất cả (noi_dia + hang_nang)')
    print(f'{len(pham_vi)} yêu cầu; {so_yeu_cau_co_ok} yêu cầu có ít nhất 1 run ok; '
          f'{so_ca_lam_lai} ca làm lại; token + tool {tien_token_tool:,.0f} đ')
    phut_lam_lai_pham_vi = pham_vi.loc[
        pham_vi['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'  trung bình phút làm lại trong phạm vi: {phut_lam_lai_pham_vi:.1f} phút/ca')
    for phut_lam_lai in (9, 15.3, phut_lam_lai_pham_vi):
        tong = (so_yeu_cau_co_ok * 5 * LUONG_PHUT
                + so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
                + tien_token_tool)
        cps = tong / thanh_cong
        print(f'  làm lại {phut_lam_lai:>4.1f} phút/ca: tổng {tong:,.0f} đ; '
              f'CPS {cps:,.0f} đ = {cps / BASELINE:.2f}x')
    for phut_lam_lai in (9, 15.3, phut_lam_lai_pham_vi):
        hoa_von = (BASELINE * thanh_cong
                   - so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
                   - tien_token_tool) / (so_yeu_cau_co_ok * LUONG_PHUT)
        print(f'  hòa vốn khi làm lại {phut_lam_lai:>4.1f} phút/ca: '
              f'mỗi lần xem lại <= {hoa_von:.1f} phút')


# ---------- Nhiệm vụ D1 · Cỡ mẫu pilot ----------
def co_mau_moi_nhom(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhánh cho phép so sánh hai tỉ lệ độc lập."""
    normal = NormalDist()
    trung_binh = (p1 + p2) / 2
    z_alpha = normal.inv_cdf(1 - alpha / 2)
    z_power = normal.inv_cdf(power)
    sai_so_gop = math.sqrt(2 * trung_binh * (1 - trung_binh))
    sai_so_rieng = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((z_alpha * sai_so_gop + z_power * sai_so_rieng) / (p2 - p1)) ** 2)


def co_mau_pilot():
    """Trả về kết quả năm câu D1 theo giả định của đề."""
    icc = 0.02
    theo_yeu_cau = co_mau_moi_nhom(0.70, 0.75)
    he_so_75 = 1 + (75 - 1) * icc
    theo_nhan_vien = math.ceil(theo_yeu_cau * he_so_75)
    muc_tieu_6_diem = co_mau_moi_nhom(0.70, 0.76)
    moi_nhan_vien = math.ceil(muc_tieu_6_diem * (1 - icc) / (20 - muc_tieu_6_diem * icc))
    he_so_6_diem = 1 + (moi_nhan_vien - 1) * icc
    return {
        'a': theo_yeu_cau,
        'b': (he_so_75, theo_nhan_vien, math.ceil(theo_nhan_vien / 75)),
        'c': int(20 / icc),
        'd': int(6 / icc),
        'e': (muc_tieu_6_diem, moi_nhan_vien, round(he_so_6_diem, 2)),
    }


# ---------- Nhiệm vụ E1 · Chỉ số đợt chạy thử ----------
def chi_so_pilot(reqs):
    """Đếm tử số và mẫu số cho E1 và tỷ lệ mở lại trong phạm vi D."""
    xem_lai = reqs.loc[reqs['duoc_xem_lai'].eq(1)]
    mo_lai = reqs['mo_lai_trong_7_ngay'].eq(1)
    trong_pham_vi = reqs['loai'].isin(['noi_dia', 'hang_nang'])
    return {
        'chinh': (int((reqs['dong_trong_24h'].eq(1) & ~mo_lai).sum()), len(reqs)),
        'bo_qua': (int(xem_lai['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()), len(xem_lai)),
        'mo_lai': (int(mo_lai.sum()), len(reqs)),
        'mo_lai_trong_pham_vi': (int((mo_lai & trong_pham_vi).sum()), int(trong_pham_vi.sum())),
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    _in_a2(ket_qua)
    _in_a3(runs, reqs)
    _in_a4(runs, reqs)
    _in_b1_b2(runs, reqs)
    _in_b3(runs, reqs)
    _in_b4(runs, reqs)

    print('\nD1 · Cỡ mẫu pilot:', co_mau_pilot())
    print('E1 · Chỉ số đợt chạy thử (tử số, mẫu số):', chi_so_pilot(reqs))
