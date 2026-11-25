# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = 82,83% |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = 27,12% |
| An toàn | Tỉ lệ lỗi lọt đến khách, đo qua mở lại | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = 4,25% |
| Dùng | Tỉ lệ yêu cầu có gợi ý hiện cho nhân viên nhánh trợ lý | Số yêu cầu đủ điều kiện có ít nhất một lần hiện gợi ý chia số yêu cầu đủ điều kiện ở nhánh trợ lý | Không cần tính |
| An toàn | Tỉ lệ hoàn sai tiền trong mẫu đối soát | Số yêu cầu có khoản hoàn khác khoản phải hoàn chia số yêu cầu đã đối soát | Không cần tính |

Đây là các chỉ số trong đợt chạy thử, tính từ CSV bằng `chi_so_pilot()` trong `src/lab13.py`. Đợt chạy thử thiếu nhóm đối chứng nên chưa thể suy ra tác động của trợ lý.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Dịch vụ yêu cầu | request_id, trace_id, created_at, arm, eligible, loai | Khi nhận yêu cầu |
| `suggestion_shown` | Giao diện CSKH | request_id, trace_id, staff_id, shown_at | Khi hiển thị gợi ý |
| `review_decided` | Giao diện CSKH | request_id, trace_id, staff_id, decision, quyết định cuối, phút xem lại | Khi nhân viên chọn giữ, sửa hoặc bỏ |
| `ticket_closed` | Dịch vụ ticket | request_id, trace_id, closed_at | Mỗi lần đóng |
| `ticket_reopened` | Dịch vụ ticket | request_id, trace_id, reopened_at, reason | Mỗi lần mở lại |
| `refund_audit_completed` | Kế toán | request_id, trace_id, số tiền đã hoàn, số tiền phải hoàn, audited_at | Khi hoàn tất đối soát từng yêu cầu |
| `staff_rework_completed` | Giao diện CSKH | request_id, trace_id, phút làm lại, reason | Khi nhân viên làm lại xong |
| `staff_manual_handling_completed` | Giao diện CSKH | request_id, trace_id, work_id, phút xử lý thủ công, luồng đối chứng hoặc chuyển người | Khi hoàn tất phần xử lý thủ công |
| `agent_run_completed` | Trợ lý | request_id, trace_id, attempt, tokens_in, tokens_out, tool_calls, status | Khi kết thúc mỗi lần chạy |
| `refund_ledger_write` | Sổ cái | request_id, trace_id, mã khoản hoàn, mã bút toán, idempotency_key, trạng thái ghi sổ | Sau mỗi lần ghi hoặc từ chối ghi |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính của pilot: ghép `refund_request_created`, `ticket_closed` và `ticket_reopened` theo `request_id`. Mẫu số gồm tất cả yêu cầu trong mẫu đã qua 8 ngày từ lúc nhận. Tử số gồm yêu cầu đóng lần đầu trong 24 giờ và không mở lại trong 7 ngày sau lần đóng đó.
- An toàn của pilot: nhóm yêu cầu đã qua 7 ngày từ lúc nhận là mẫu số. Tử số là số yêu cầu trong nhóm có ít nhất một `ticket_reopened` trong 7 ngày đầu kể từ lúc nhận. So hai nhánh cùng cửa sổ. Số 51/1.200 chỉ tái lập cờ lịch sử từ CSV, vốn thiếu dấu thời gian để xác minh mốc bắt đầu theo dõi.
- Tỉ lệ bỏ qua: đếm một quyết định cuối trong `review_decided` cho mỗi yêu cầu. Mẫu số gồm yêu cầu được nhân viên xem lại.
- Tỉ lệ hiện gợi ý: ghép `refund_request_created` và `suggestion_shown`, đếm theo yêu cầu đủ điều kiện của nhánh trợ lý.
- Tỉ lệ hoàn sai: dùng `refund_audit_completed`, đối chiếu hai khoản tiền cho mỗi yêu cầu trong mẫu.
- Gắn `trace_id` ngay khi nhận yêu cầu, kể cả nhánh đối chứng. Khi một yêu cầu có nhiều lần chạy, dùng cùng mã liên kết và phân biệt bằng `attempt`.
- Luật dừng do hoàn trùng dùng `refund_ledger_write`, đếm các bút toán thành công có mã bút toán khác nhau cho cùng mã khoản hoàn.
- Chi phí cả hệ thống: ghép lượt chạy, xem lại, làm lại và xử lý thủ công theo `request_id`. Mỗi thao tác lao động chỉ được ghi ở một loại sự kiện. Cộng chi phí trên tất cả yêu cầu đủ điều kiện, kể cả yêu cầu chuyển nhân viên, rồi chia cho số yêu cầu đó.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Tần suất làm lại tăng | B1: Làm lại gấp đôi làm chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** [simulated] (`bang_chi_phi.md`). | Tỉ lệ yêu cầu có lần làm lại theo loại và theo tuần. | Phân tích nguyên nhân theo loại trước khi mở rộng pilot. | PM trợ lý hoàn phí |
| Phải xem lại toàn bộ kéo dài | B4: Xem lại 100% (`noi_dia` + `hang_nang`) tốn **11.743 đ/việc thành công** với 9 phút làm lại hoặc **12.415 đ/việc thành công** với 15,3 phút [simulated]. | Tỉ lệ có người xem lại, phút lao động đo thật, kết quả đối soát sai tiền và hoàn trùng, tỷ lệ mở lại. | Thử giảm theo bậc ở ca nội địa chuẩn. Chỉ duy trì mức xem lại thấp hơn khi an toàn đạt và chi phí thực của cả hệ thống dưới 12.000 đ/yêu cầu theo [kế hoạch pilot](pilot_plan.yaml). | Trưởng nhóm CSKH |
