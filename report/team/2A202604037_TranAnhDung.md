# Báo cáo cá nhân — TranAnhDung-2A202604037

## 1. Thông tin thành viên

- Họ tên: Trần Anh Dũng
- MSSV: 2A202604037
- Email: dungkidx01@gmail.com
- GitHub: tad-4963
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Thực hiện gắn nhãn độc lập 20 ca lỗi ở CP3 trước khi đối chiếu với Người gắn nhãn 1 (Phạm Trấn Quốc).
- Giữ và cập nhật dần hồ sơ [ho_so_launch_v0.md](ho_so_launch_v0.md) từ đầu buổi, đảm bảo gắn đủ nhãn `simulated`, tuân thủ quy tắc 5 (chỉ duyệt kế hoạch pilot), mỗi mục có một vai trò phụ trách cụ thể.
- Phối hợp với Quốc hoàn thiện bảng lỗi và bảng khắc phục 5 ca trong [bang_loi.md](bang_loi.md), cùng nhóm hoàn thiện rủi ro kinh tế (E2), duyệt chéo Gate 2a và báo cáo nhóm.

## 3. Đóng góp cụ thể

- **CP3 (Gắn nhãn độc lập):** Hoàn thành phiếu gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR tại [CP3_phieu_TranAnhDung.md](../../docs/CP3_phieu_TranAnhDung.md) (4 ca Do người dùng, 5 ca Hệ thống, 4 ca Ngữ cảnh, 4 ca Giới hạn hệ thống, 3 ca Ngầm).
- **Hồ sơ launch v0 (E3):** Cập nhật thông tin nhóm/lớp và điền số liệu các mục 1, 2, 3, 7 từ [bang_chi_phi.md](bang_chi_phi.md) vào [ho_so_launch_v0.md](ho_so_launch_v0.md), gắn nhãn `simulated`, chuẩn hoá vai trò phụ trách theo quyền quyết định tại LogiX-VN.
- **Rủi ro kinh tế (E2):** Cập nhật số liệu tác động từ B1 (+51,8%, lên 6.787 đ `simulated`) và B4 (11.743 đ = 0,98× / 12.415 đ = 1,03× `simulated`) vào bảng E2 trong [chi_so.md](chi_so.md).
- **Đối chiếu CP3 & Duyệt chéo Gate 2a:** *(cập nhật sau khi đối chiếu với Quốc và hoàn tất duyệt chéo lúc 17:00–17:45)*.

## 4. Bằng chứng

- Commit `97505fa`: `docs(cp3): add independent labeling sheet for Tran Anh Dung` — [CP3_phieu_TranAnhDung.md](../../docs/CP3_phieu_TranAnhDung.md).
- Các mục 1, 2, 3, 7 và đề xuất trong [ho_so_launch_v0.md](ho_so_launch_v0.md).
- Bảng rủi ro kinh tế E2 trong [chi_so.md](chi_so.md).
- *(Bổ sung mã commit sau khi đối chiếu CP3 và chốt hồ sơ cuối buổi)*.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (Gemini).
- **Dùng vào việc gì:** Đọc nhanh cấu trúc repo và yêu cầu lab, lập kế hoạch công việc theo vai trò, giải thích phân biệt 5 loại lỗi Google PAIR, hỗ trợ tổng hợp số liệu đã tính từ `bang_chi_phi.md` vào `ho_so_launch_v0.md` và bảng E2 trong `chi_so.md`, kiểm tra quy tắc định dạng (nhãn `simulated`, tuân thủ quy tắc 5 của lab).
- **Cách tự kiểm tra:** Đối chiếu từng con số đưa vào hồ sơ với kết quả trong `report/team/bang_chi_phi.md` và `src/lab13.py`; rà lại từng ca trong 20 ca lỗi theo nguyên nhân gốc trước khi gửi đối chiếu với Quốc; kiểm tra thủ công trạng thái và vai trò phụ trách từng mục.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ phần gắn nhãn độc lập CP3 và giữ nhịp cập nhật hồ sơ ngay khi nhóm có số liệu A/B.
- Cần theo sát mốc đối chiếu CP3 với Quốc và rà soát toàn bộ `report/team/` trước 17:00 để bảo vệ tốt tại phiên duyệt chéo Gate 2a.
