# Team

## Thông tin nhóm

- Tên nhóm: Ghidorah
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Ghidorah-LaunchEconomics`
- URL repo: [github.com/Quoosc/K5-L3B-DAY13-Ghidorah-LaunchEconomics](https://github.com/Quoosc/K5-L3B-DAY13-Ghidorah-LaunchEconomics)
- Nhánh nộp: `main`
- Commit chốt: cập nhật mã commit cuối trước khi nộp.

## Thành viên và phân công

| STT | Họ tên                | MSSV        | Email                      | GitHub        | Vai trò                                         |
| --: | --------------------- | ----------- | -------------------------- | ------------- | ----------------------------------------------- |
|   1 | Phạm Trấn Quốc        | 2A202604113 | Chưa cập nhật              | Quoosc        | Người gắn nhãn 1; trưởng nhóm                   |
|   2 | Trương Văn Phong      | 2A202604091 | 26ai.phongtv@vinuni.edu.vn | vanphong205   | Người viết code ở nửa đầu buổi                  |
|   3 | Nguyễn Quốc Quang Anh | 2A202604120 | nguyenquocquanganh28@gmail.com | QuangAnh28    | Người kiểm số; nhận phần viết code sau giải lao |
|   4 | Trần Anh Dũng         | 2A202604037 | dungkidx01@gmail.com           | tad-4963      | Người gắn nhãn 2, kiêm giữ hồ sơ                |

### Phạm vi công việc theo vai

- **Phạm Trấn Quốc — người gắn nhãn 1:** mở [phiếu trắng CP3](docs/CP3_phieu_gan_nhan_trang.md), tạo một bản riêng và ghi đủ 20 nhãn trong 8 phút. Khi cả hai đã hoàn tất, nhận bộ nhãn gốc của Dũng, đối chiếu và lưu kết quả trong [bảng lỗi](report/team/bang_loi.md). Ghi đóng góp thực tế và bằng chứng vào [báo cáo cá nhân](report/team/2A202604113_PhamTranQuoc.md).
- **Trần Anh Dũng — người gắn nhãn 2, kiêm giữ hồ sơ:** mở cùng [phiếu trắng CP3](docs/CP3_phieu_gan_nhan_trang.md) nhưng làm trên bản riêng trong 8 phút. Khi cả hai đã hoàn tất, gửi Quốc đủ 20 cặp mã ca và nhãn để đối chiếu. Cập nhật [hồ sơ launch](report/team/ho_so_launch_v0.md) khi có bằng chứng.
- **Trương Văn Phong — người viết code A/B:** code A/B có ở commit `dc8e753`. Xem [bảng chi phí](report/team/bang_chi_phi.md) và kết quả chạy được ghi trong [báo cáo của Phong](report/team/2A202604091_TruongVanPhong.md). Phong phụ trách bàn giao commit cùng log chạy cho Quang Anh.
- **Nguyễn Quốc Quang Anh — người kiểm số và nhận code:** mở [bảng chi phí](report/team/bang_chi_phi.md) và [công thức](docs/du_lieu_va_cong_thuc.md). Tính tay ít nhất một số A/B, ghi công thức, đầu vào và kết quả vào báo cáo cá nhân. Đối chiếu với bảng và log của Phong, sau đó nhận [code A/B](src/lab13.py) và chạy lại trên máy của mình.
- **Cả nhóm:** cùng hoàn thiện [pilot](report/team/pilot_plan.yaml), [chỉ số](report/team/chi_so.md), [phiếu duyệt chéo](report/team/phieu_cham.md) và [báo cáo nhóm](report/team/group_report.md). Gắn nhãn `simulated` cho mọi số dùng cột `_simulated`.

Quốc và Dũng chỉ mở phần tham khảo và so nhãn sau khi cả hai đã hoàn tất hai bộ nhãn riêng. Giữ nguyên hai bộ gốc khi nhập kết quả.

**Trạng thái bàn giao.** Commit A/B `dc8e753` đã có trong nhánh local tại `1fd01ef`. Ngày 25/11/2026, Codex đã tính lại tiền tool từ CSV và chạy `lab13.py` từ đầu đến cuối trên máy, đạt cả ba phép thử A1. Kết quả A/B, D1 và E1 đã được đối chiếu. Quang Anh đã kiểm tra lại và xác nhận kết quả khớp với các số đối chiếu. Dũng đã nộp phiếu CP3 ở commit `97505fa`. Còn chờ phiếu độc lập của Quốc, đối chiếu CP3 và kết quả hội đồng. Việc tuyển đủ nhân lực cho pilot và việc nộp LMS chưa được xác nhận.

## Báo cáo đóng góp cá nhân

Mỗi thành viên tạo một file theo mẫu `report/team/MSSV_HoTen.md` (không dấu), ghi đóng góp thực tế và bằng chứng sau khi hoàn thành. Các mục dưới đây là phân công dự kiến, chưa phải xác nhận công việc đã hoàn thành.

### Phạm Trấn Quốc — 2A202604113

**Phần việc phụ trách:** Người gắn nhãn 1; điều phối nhóm và theo dõi tiêu chí hoàn thành.

**Đóng góp cần thực hiện:** Gắn nhãn độc lập 20 ca ở CP3; tham gia thống nhất các ca bất đồng và rà điều kiện hoàn thành của hồ sơ.

**Tiến độ và bằng chứng:** Đã có [phiếu trắng CP3](docs/CP3_phieu_gan_nhan_trang.md), phần tham khảo, kết quả D1/E1 và bản dự thảo hồ sơ nhóm do Sol (Codex) hỗ trợ. Dũng đã nộp phiếu riêng. Còn chờ phiếu độc lập của Quốc và phần đối chiếu. Xem [danh sách việc của Quốc](report/team/2A202604113_PhamTranQuoc.md#danh-sách-việc-của-quốc).

### Trương Văn Phong — 2A202604091

**Phần việc phụ trách:** Người viết code ở nửa đầu buổi, nhiệm vụ A và B.

**Đóng góp cần thực hiện:** Hoàn thiện và chạy `src/lab13.py`; phối hợp điền `report/team/bang_chi_phi.md`; bàn giao phần code sau giải lao.

**Bằng chứng cần ghi:** Commit và phần code/bảng đã thực hiện; kết quả các phép thử A1; công cụ AI đã dùng và cách tự kiểm tra (nếu có).

### Nguyễn Quốc Quang Anh — 2A202604120

**Phần việc phụ trách:** Kiểm số ở nửa đầu buổi, nhận phần viết/chạy code sau giải lao.

**Đóng góp cần thực hiện:** Tính tay ít nhất một con số để đối chiếu; rà số liệu A/B; sau giải lao tiếp nhận, chạy lại hoặc hoàn thiện code và phối hợp với nhóm ở D/E.

**Tiến độ và bằng chứng.** [Báo cáo cá nhân](report/team/2A202604120_NguyenQuocQuangAnh.md) ghi phép tính tiền tool từ CSV, mốc so sánh A/B và kết quả chạy lại do Codex hỗ trợ. Đã kiểm tra lại và xác nhận kết quả khớp. Số đã đối chiếu được cập nhật vào bảng chi phí, phần rủi ro E2 và hồ sơ launch.

### Trần Anh Dũng — 2A202604037

**Phần việc phụ trách:** Người gắn nhãn 2, kiêm giữ hồ sơ.

**Đóng góp cần thực hiện:** Điền dần `report/team/ho_so_launch_v0.md`; gắn nhãn độc lập 20 ca ở CP3; phối hợp hoàn thiện bảng lỗi và hồ sơ cuối.

**Tiến độ và bằng chứng:** Đã hoàn thành phiếu gắn nhãn độc lập 20 ca lỗi tại [CP3_phieu_TranAnhDung.md](docs/CP3_phieu_TranAnhDung.md) (commit `97505fa`), cập nhật [hồ sơ launch](report/team/ho_so_launch_v0.md), phần rủi ro E2 trong [chỉ số](report/team/chi_so.md) và lập [báo cáo cá nhân](report/team/2A202604037_TranAnhDung.md). Đang chờ bộ nhãn độc lập của Quốc để đối chiếu CP3 vào [bảng lỗi](report/team/bang_loi.md) và chốt hồ sơ trước 17:00.
