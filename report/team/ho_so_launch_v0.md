# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Ghidorah · Lớp: L3B-E305

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | A2: 4.472 đ/việc trên 978 việc thành công [simulated], gấp 16,3× hoá đơn token+tool/yêu cầu (274,7 đ). A4 phạm vi `noi_dia` + `hang_nang` gồm cố định 40tr/tháng: 4.599 đ = 0,38× [simulated] (nửa khối lượng: 5.784 đ = 0,48×). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | B1/B2: 1. Làm lại gấp đôi +51,8% (lên 6.787 đ) · 2. Xem lại gấp đôi +40,7% (lên 6.292 đ) · 3. Lương nhân viên tăng 25% làm chi phí tăng +23,1% (lên 5.506 đ) [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Mốc 12.000 đ/yêu cầu. B3 cả hệ thống tối ưu ở 2 lần chạy: 6.901.220 đ/1.200 yêu cầu ≈ 5.751 đ/yêu cầu = 0,48× (3 lần chạy: 5.865 đ = 0,49×) [simulated]. `noi_dia` 0,22×, `hang_nang` 0,69×; loại `quoc_te` (1,88×) & `doi_tac` (0,85×). B4 xem lại 100%: 11.743 đ = 0,98× (15,3 phút làm lại: 12.415 đ = 1,03×) [simulated]. | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (chưa có đối chứng): 82,83% đóng trong 24h và không mở lại 7 ngày, 27,12% sửa hoặc bỏ gợi ý, 4,25% mở lại 7 ngày; 9 event có `trace_id`. | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đã có phiếu gắn nhãn độc lập của người 2 (`CP3_phieu_TranAnhDung.md`) và khung 5 khắc phục tham khảo. Chờ đối chiếu đủ hai bộ nhãn độc lập và chốt tỉ lệ đồng thuận. | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia cụm theo nhân viên: 20 người/nhánh, 5.980 yêu cầu thô (859,20 hiệu dụng), MDE 6 điểm (đánh đổi: nếu hiệu ứng thật 5 điểm, power ~64,18%). Mẫu lịch sử có 20 người; cần xác nhận tuyển đủ 40 người; 4 luật dừng đủ 4 vế. | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: +51,8% lên 6.787 đ [simulated]. Xem lại 100% kéo dài: 11.743 đ = 0,98× (9 phút) hoặc 12.415 đ = 1,03× (15,3 phút làm lại) [simulated]; hoà vốn khi xem lại ≤ 5,1 phút (≤ 4,8 phút ở 15,3 phút). | Giả lập | PM trợ lý hoàn phí |

**Đề xuất hiện tại: No-go** *(trạng thái trước duyệt chéo)*. Trình lại Gate 2a khi hoàn tất: (1) đối chiếu đủ hai bộ nhãn độc lập CP3 và bảng khắc phục 5 ca (`Kỹ sư trưởng agent`, trước 17:00), (2) xác nhận đủ 40 nhân viên (20/nhánh) và ký chấp nhận đánh đổi MDE từ 5 lên 6 điểm (`Giám đốc vận hành LogiX-VN`, trước ngày khởi động pilot), (3) phương án giảm tỉ lệ xem lại theo bậc (do xem lại 100% với 15,3 phút làm lại vượt mốc 12.000 đ [simulated]) và thay số phút `simulated` bằng đo thật sau tuần 1 (`Trưởng nhóm CSKH`, cuối tuần 1 pilot).
