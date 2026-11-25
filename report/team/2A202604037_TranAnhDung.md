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
- **Đối chiếu CP3 và duyệt chéo Gate 2a:** Đối chiếu theo mã cho thấy phiếu gốc của Dũng trùng 20/20 với phiếu Quốc xác nhận từ nhãn tham khảo. [Bảng lỗi](bang_loi.md) ghi riêng tình trạng bằng chứng đồng thuận độc lập. Rà phản hồi cho năm câu hỏi trao đổi với ToiYeuVinFast trong [phiếu chấm](phieu_cham.md) và kiểm tra bản chạy, YAML, nhãn `simulated` và quy tắc 5 trước khi nộp.

## 4. Bằng chứng

- Commit `97505fa`: `docs(cp3): add independent labeling sheet for Tran Anh Dung` — [CP3_phieu_TranAnhDung.md](../../docs/CP3_phieu_TranAnhDung.md).
- Commit `0fc3bbe` cập nhật [hồ sơ launch](ho_so_launch_v0.md) và [bảng rủi ro E2](chi_so.md). Commit `9c02779` ghi kết quả đối chiếu tham khảo tại [bảng lỗi](bang_loi.md). Commit `77943af` ghi lần rà cuối của Dũng.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (Gemini).
- **Dùng vào việc gì:** Đọc nhanh cấu trúc repo và yêu cầu lab, lập kế hoạch công việc theo vai trò, giải thích phân biệt 5 loại lỗi Google PAIR, hỗ trợ tổng hợp số liệu đã tính từ `bang_chi_phi.md` vào `ho_so_launch_v0.md` và bảng E2 trong `chi_so.md`, kiểm tra quy tắc định dạng (nhãn `simulated`, tuân thủ quy tắc 5 của lab) và chạy checklist rà soát trước khi nộp.
- **Cách tự kiểm tra:** Đối chiếu từng con số đưa vào hồ sơ với kết quả chạy trực tiếp `src/lab13.py` và `report/team/bang_chi_phi.md`; rà lại từng ca trong 20 ca lỗi theo nguyên nhân gốc trước khi đối chiếu với Quốc; chạy `yaml.safe_load` trên `pilot_plan.yaml` và quét kiểm tra toàn bộ `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ vai trò Người gắn nhãn 2 kiêm giữ hồ sơ: nộp phiếu gắn nhãn độc lập 20 ca CP3 sớm, giữ hồ sơ `ho_so_launch_v0.md` đồng bộ với số liệu A/B/D/E của nhóm, đảm bảo đủ nhãn `simulated`, vai trò phụ trách rõ ràng và không vi phạm quy tắc 5.
- Điểm cần rút kinh nghiệm: cần thống nhất sớm hơn quy trình nộp phiếu độc lập của cả hai người gắn nhãn trước khi mở tài liệu tham khảo để bằng chứng đồng thuận độc lập CP3 được trọn vẹn ngay từ lần đầu.
