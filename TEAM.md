# Team

## Thông tin nhóm

- Tên nhóm: Ghidorah
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Ghidorah-LaunchEconomics`
- URL repo: [github.com/Quoosc/K5-L3B-DAY13-Ghidorah-LaunchEconomics](https://github.com/Quoosc/K5-L3B-DAY13-Ghidorah-LaunchEconomics)
- Nhánh nộp: `main`
- Commit chốt: cập nhật mã commit cuối trước khi nộp.

## Thành viên và phân công

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Phạm Trấn Quốc | 2A202604113 | Chưa cập nhật | Quoosc | Người gắn nhãn 1; trưởng nhóm |
| 2 | Trương Văn Phong | 2A202604091 | Chưa cập nhật | Chưa cập nhật | Người viết code ở nửa đầu buổi |
| 3 | Nguyễn Quốc Quang Anh | 2A202604120 | Chưa cập nhật | Chưa cập nhật | Người kiểm số; nhận phần viết code sau giải lao |
| 4 | Trần Anh Dũng | 2A202604037 | Chưa cập nhật | Chưa cập nhật | Người gắn nhãn 2, kiêm giữ hồ sơ |

### Phạm vi công việc theo vai

- **Phạm Trấn Quốc — người gắn nhãn 1:** mở [phiếu trắng CP3](docs/CP3_phieu_gan_nhan_trang.md), tạo một bản riêng và ghi đủ 20 nhãn trong 8 phút. Khi cả hai đã hoàn tất, nhận bộ nhãn gốc của Dũng, đối chiếu và lưu kết quả trong [bảng lỗi](report/team/bang_loi.md). Ghi đóng góp thực tế và bằng chứng vào [báo cáo cá nhân](report/team/2A202604113_PhamTranQuoc.md).
- **Trần Anh Dũng — người gắn nhãn 2, kiêm giữ hồ sơ:** mở cùng [phiếu trắng CP3](docs/CP3_phieu_gan_nhan_trang.md) nhưng làm trên bản riêng trong 8 phút. Khi cả hai đã hoàn tất, gửi Quốc đủ 20 cặp mã ca và nhãn để đối chiếu. Cập nhật [hồ sơ launch](report/team/ho_so_launch_v0.md) khi có bằng chứng.
- **Trương Văn Phong — người viết code A/B:** mở [lab13.py](src/lab13.py#L20). Bắt đầu ở `TODO CP1` với `so_lan_chay_ky_vong()` và hai hàm A1 còn lại, rồi làm A2–A4 và `TODO CP2` cho B. Chạy `python lab13.py` từ `src/`, điền [bảng chi phí](report/team/bang_chi_phi.md) và bàn giao commit cùng log chạy cho Quang Anh.
- **Nguyễn Quốc Quang Anh — người kiểm số và nhận code:** mở [bảng chi phí](report/team/bang_chi_phi.md) và [công thức](docs/du_lieu_va_cong_thuc.md). Tính tay ít nhất một số A/B, ghi công thức, đầu vào và kết quả vào báo cáo cá nhân. Đối chiếu với bảng và log của Phong, sau đó nhận [code A/B](src/lab13.py) và chạy lại trên máy của mình.
- **Cả nhóm:** cùng hoàn thiện [pilot](report/team/pilot_plan.yaml), [chỉ số](report/team/chi_so.md), [phiếu duyệt chéo](report/team/phieu_cham.md) và [báo cáo nhóm](report/team/group_report.md). Gắn nhãn `simulated` cho mọi số dùng cột `_simulated`.

Quốc và Dũng chỉ mở phần tham khảo và so nhãn sau khi cả hai đã hoàn tất hai bộ nhãn riêng. Giữ nguyên hai bộ gốc khi nhập kết quả.

**Trạng thái bàn giao:** D1/E1 chạy được riêng. Luồng chính hiện dừng ở phép thử A1 đầu tiên với `NotImplementedError` tại `so_lan_chay_ky_vong()`. Hai bộ nhãn, đóng góp cá nhân của Quốc, kết quả hội đồng, xác nhận đủ nhân lực và nộp LMS đang chờ bằng chứng.

## Báo cáo đóng góp cá nhân

Mỗi thành viên tạo một file theo mẫu `report/team/MSSV_HoTen.md` (không dấu), ghi đóng góp thực tế và bằng chứng sau khi hoàn thành. Các mục dưới đây là phân công dự kiến, chưa phải xác nhận công việc đã hoàn thành.

### Phạm Trấn Quốc — 2A202604113

**Phần việc phụ trách:** Người gắn nhãn 1; điều phối nhóm và theo dõi tiêu chí hoàn thành.

**Đóng góp cần thực hiện:** Gắn nhãn độc lập 20 ca ở CP3; tham gia thống nhất các ca bất đồng và rà điều kiện hoàn thành của hồ sơ.

**Tiến độ và bằng chứng:** Đã có [phiếu trắng CP3](docs/CP3_phieu_gan_nhan_trang.md), phần tham khảo, kết quả D1/E1 và bản dự thảo hồ sơ nhóm do Sol (Codex) hỗ trợ. Còn chờ hai bộ nhãn độc lập và phần đối chiếu. Xem [danh sách việc của Quốc](report/team/2A202604113_PhamTranQuoc.md#danh-sách-việc-của-quốc).

### Trương Văn Phong — 2A202604091

**Phần việc phụ trách:** Người viết code ở nửa đầu buổi, nhiệm vụ A và B.

**Đóng góp cần thực hiện:** Hoàn thiện và chạy `src/lab13.py`; phối hợp điền `report/team/bang_chi_phi.md`; bàn giao phần code sau giải lao.

**Bằng chứng cần ghi:** Commit và phần code/bảng đã thực hiện; kết quả các phép thử A1; công cụ AI đã dùng và cách tự kiểm tra (nếu có).

### Nguyễn Quốc Quang Anh — 2A202604120

**Phần việc phụ trách:** Kiểm số ở nửa đầu buổi, nhận phần viết/chạy code sau giải lao.

**Đóng góp cần thực hiện:** Tính tay ít nhất một con số để đối chiếu; rà số liệu A/B; sau giải lao tiếp nhận, chạy lại hoặc hoàn thiện code và phối hợp với nhóm ở D/E.

**Bằng chứng cần ghi:** Phép tính tay và kết quả đối chiếu; commit và phần code/bảng đã thực hiện; công cụ AI đã dùng và cách tự kiểm tra (nếu có).

### Trần Anh Dũng — 2A202604037

**Phần việc phụ trách:** Người gắn nhãn 2, kiêm giữ hồ sơ.

**Đóng góp cần thực hiện:** Điền dần `report/team/ho_so_launch_v0.md`; gắn nhãn độc lập 20 ca ở CP3; phối hợp hoàn thiện bảng lỗi và hồ sơ cuối.

**Bằng chứng cần ghi:** Bộ nhãn người 2 trong `report/team/bang_loi.md`; các mục/commit đã điền trong hồ sơ; công cụ AI đã dùng và cách tự kiểm tra (nếu có).
