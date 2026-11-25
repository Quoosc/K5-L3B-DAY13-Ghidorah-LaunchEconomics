# Báo cáo cá nhân — Nguyễn Quốc Quang Anh — 2A202604120

**Tình trạng.** Đã tính lại từ CSV, chạy hết chương trình trên máy và xác minh commit A/B đã có trong nhánh local. Lượt kiểm tra ngày 25/11/2026 do Codex thực hiện theo yêu cầu.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Quốc Quang Anh
- MSSV: 2A202604120
- Email: nguyenquocquanganh28@gmail.com
- GitHub: QuangAnh28
- Vai trong nhóm: Người kiểm số, tiếp nhận phần code sau giải lao.

## 2. Phần việc phụ trách

Theo [TEAM.md](../../TEAM.md), nhiệm vụ là tính ít nhất một con số chi phí để đối chiếu, rà bảng A/B, tiếp nhận code từ Phong sau giải lao và phối hợp ở D/E.

## 3. Đóng góp cụ thể

- Codex tính độc lập các mốc A/B từ hai CSV và so với kết quả in từ code nhóm ở commit `1fd01ef`.
- Codex đối chiếu năm câu D1 và ba chỉ số E1. Kết quả nằm trong [kế hoạch pilot](pilot_plan.yaml) và [đặc tả chỉ số](chi_so.md).
- Codex rà nhãn `simulated` trong [bảng chi phí](bang_chi_phi.md) và cập nhật số A/B vào phần rủi ro E2, [hồ sơ launch](ho_so_launch_v0.md) và [báo cáo nhóm](group_report.md).

## 4. Bằng chứng

**Phép tính đối chiếu A2.** Codex cộng cột `tool_calls` của 1.624 dòng trong [logix_runs.csv](../../src/logix_runs.csv) bằng PowerShell, gồm cả các lần chạy lỗi.

| Lượt thử | Số lần chạy | Số lần gọi tool |
| --- | ---: | ---: |
| 1 | 1.200 | 4.143 |
| 2 | 258 | 887 |
| 3 | 166 | 570 |
| Tổng | 1.624 | 5.600 |

Theo [bảng đơn giá](../../docs/du_lieu_va_cong_thuc.md), tiền tool bằng **(4.143 + 887 + 570) × 15 = 84.000 đ**. Kết quả khớp dòng Tool của A2 trong bảng nhóm, kết quả chạy code và [báo cáo của Phong](2A202604091_TruongVanPhong.md).

**Các mốc rà A/B.** Cột chi phí và phần trăm thay đổi dưới đây sử dụng hai cột phút giả lập hoặc giả định thời gian tại B4. Các giá trị đó được ghi nhãn `simulated`.

| Mục | Số đối chiếu tính từ dữ liệu và giả định của lab |
| --- | --- |
| A2 | 978 việc thành công. Tổng 4.373.585,13 đ / 978 = 4.471,97 đ/việc (`simulated`). Hóa đơn token và tool là 274,65 đ/yêu cầu. |
| A3 | Chi phí mỗi việc thành công của nội địa, hàng nặng, quốc tế, đối tác lần lượt khoảng 2.696 đ, 8.221 đ, 22.515 đ, 10.215 đ (`simulated`). |
| A4 | Sau cộng chi phí cố định, khoảng 4.599 đ/việc ở 45.000 yêu cầu/tháng và 5.784 đ/việc ở 22.500 yêu cầu/tháng (`simulated`). |
| B1 | Giá token ×2 / ÷2: +5,6% / −2,8%. Xem lại ×2 / ÷2: +40,7% / −20,3%. Làm lại ×2 / ÷2: +51,8% / −25,9%. Lương +25%: +23,1%. Giới hạn 2 / 1 lượt: −5,2% / −8,1% (`simulated`). |
| B2 | Token và xem lại cùng gấp đôi: khoảng 6.543 đ/việc, +46,3% (`simulated`). |
| B3 | Giới hạn 2 lượt có tổng chi phí hệ thống khoảng 6.901.220 đ, tức khoảng 5.751 đ/yêu cầu so với mốc 12.000 đ. Giới hạn 1 lượt có chi phí mỗi việc thành công thấp nhất, khoảng 4.111 đ, và thêm 85 yêu cầu không thành công so với giới hạn 2. Các chi phí mới là `simulated`. |
| B4 | Kịch bản xem lại 100% tính trên 948 yêu cầu có run `ok`, 48 ca làm lại và 900 việc thành công. Chi phí khoảng 11.743 đ/việc với 9 phút làm lại, 12.415 đ/việc với 15,3 phút và 12.516 đ/việc với trung bình giả lập 16,25 phút trong phạm vi (`simulated`). |

**Cách tái lập.** Chạy từ thư mục `src/`. Đoạn PowerShell cộng số gọi tool theo từng lượt thử từ CSV. Lệnh Python dùng môi trường đã cài [requirements.txt](../../src/requirements.txt) để chạy các bảng A/B, D1 và E1.

```powershell
$tongTheoLuot = Import-Csv logix_runs.csv | Group-Object attempt | ForEach-Object {
    [pscustomobject]@{ Luot = $_.Name; SoLanGoi = ($_.Group | Measure-Object tool_calls -Sum).Sum }
}
$tongTheoLuot
($tongTheoLuot | Measure-Object SoLanGoi -Sum).Sum * 15
python -X utf8 -B lab13.py
```

Codex đã chạy [lab13.py](../../src/lab13.py) ở commit nhóm `1fd01ef` bằng Python đi kèm Codex. Chương trình kết thúc với mã 0 và in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25). A2 in 84.000 đ tiền tool. D1 cho 1.251 yêu cầu mỗi nhánh nếu chia theo yêu cầu, và 299 yêu cầu mỗi người nếu chia theo 20 nhân viên mỗi nhánh để phát hiện chênh lệch 6 điểm. E1 cho 994/1.200, 48/177 và 51/1.200.

**Bằng chứng bàn giao qua Git.** Lệnh `git merge-base --is-ancestor dc8e753 HEAD` trả mã 0. Commit A/B `dc8e753` đã nằm trong lịch sử nhánh local tại `1fd01ef`, kèm code, bảng chi phí và báo cáo của Phong có lệnh chạy, kết quả. Lượt chạy ngày 25/11/2026 là bằng chứng chạy lại trên bản code đã pull. Việc hai thành viên trao đổi log riêng chưa được xác nhận.

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc đề, soạn bản code D1/E1 để đối chiếu, tính từ CSV, chạy bản code nhóm và cập nhật báo cáo. Kết quả D1 được so với hướng dẫn buổi chiều. Tiền tool và ba chỉ số E1 được kiểm tra bằng hai phép đếm riêng, một bằng mô-đun `csv` và một bằng code nhóm dùng `pandas`.

Thành viên xác nhận chưa tự tính hoặc tự chạy lại. Các số ở mục 4 ghi lại kết quả Codex đã kiểm tra.

## 6. Tự đánh giá

Kết quả Codex kiểm chứng cho thấy phép tính A2 tái lập được từ CSV và code đã pull chạy hết A/B, D1 và E1. Thành viên có thể dùng lại các lệnh ở mục 4 để tự kiểm tra theo phân công. Bằng chứng này ghi lượt kiểm tra của Codex.
