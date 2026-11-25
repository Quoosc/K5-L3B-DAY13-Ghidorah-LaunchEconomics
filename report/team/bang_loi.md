# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Trấn Quốc · Người gắn nhãn 2: Trần Anh Dũng

Mỗi người lập bộ 20 nhãn riêng trong 8 phút, giữ riêng cho đến khi cả hai đã hoàn tất. Sau đó chép nguyên hai bộ vào bảng. Mọi thay đổi sau khi thảo luận được ghi ở cột “Nhãn thống nhất”.

**Nhận phiếu:** Cột Dũng được chép theo mã ca từ [phiếu gốc](../../docs/CP3_phieu_TranAnhDung.md) tại commit `97505fa`. Dấu — biểu thị ô đang chờ dữ liệu. Chờ phiếu độc lập của Quốc. Dùng [phiếu trắng CP3](../../docs/CP3_phieu_gan_nhan_trang.md) khi làm riêng. Trước khi nhập, kiểm đủ mã 01–20 đúng một lần cho mỗi người và kiểm nhãn thuộc năm loại trên.

| Ca | Quốc (phiếu cá nhân) | Dũng (phiếu cá nhân) | Trùng? | Nhãn thống nhất Quốc–Dũng |
| --: | --- | --- | --- | --- |
| 1 | — | Do người dùng | — | — |
| 2 | — | Hệ thống | — | — |
| 3 | — | Ngữ cảnh | — | — |
| 4 | — | Giới hạn hệ thống | — | — |
| 5 | — | Ngầm | — | — |
| 6 | — | Do người dùng | — | — |
| 7 | — | Hệ thống | — | — |
| 8 | — | Hệ thống | — | — |
| 9 | — | Do người dùng | — | — |
| 10 | — | Ngữ cảnh | — | — |
| 11 | — | Giới hạn hệ thống | — | — |
| 12 | — | Ngầm | — | — |
| 13 | — | Giới hạn hệ thống | — | — |
| 14 | — | Do người dùng | — | — |
| 15 | — | Hệ thống | — | — |
| 16 | — | Ngữ cảnh | — | — |
| 17 | — | Ngầm | — | — |
| 18 | — | Ngữ cảnh | — | — |
| 19 | — | Giới hạn hệ thống | — | — |
| 20 | — | Hệ thống | — | — |

**Đồng thuận Quốc–Dũng** chưa tính được vì mới có một phiếu gốc.

**Mã ca bất đồng:** Xác định sau khi nhận phiếu của Quốc và so hai bộ gốc.

**Tỉ lệ khớp đáp án giảng viên:** Chờ đáp án chính thức và nhãn thống nhất.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Năm biện pháp đề xuất từ các tình huống trong đề, để nhóm xem xét khi chốt CP3 và chuẩn bị pilot.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Vai trò phụ trách đề xuất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Đếm sự kiện `refund_destination_invalid` theo ngày và rà mỗi ca lệnh đã gửi nhưng bị ngân hàng từ chối vì định dạng tài khoản. | Kiểm tra định dạng theo ngân hàng trước khi gửi lệnh và yêu cầu khách sửa thông tin. | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát hằng ngày và cảnh báo khi cùng mã giao dịch hoàn nghiệp vụ có từ hai bút toán hoàn thành công. | Dùng cùng khóa chống trùng cho các lần gửi lại của một giao dịch và trả trạng thái lệnh hiện có. | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Đếm mỗi ngày số thông báo hoàn tiền gửi trong khung giờ yên tĩnh theo giờ địa phương của khách. | Xếp thông báo vào hàng đợi và gửi khi hết khung giờ yên tĩnh. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Theo dõi hằng tuần số sự kiện `unsupported_input` có kiểu đầu vào là âm thanh và số ca khách gửi lại bằng văn bản. | Báo rõ kênh chưa xử lý giọng nói và hướng dẫn gửi văn bản hoặc chuyển nhân viên. | PM trợ lý hoàn phí |
| 5 | Ngầm | Đối soát hằng tuần số đơn có mã giảm giá mà khoản hoàn vượt số tính theo phí thực trả. | Tính trên khoản phí đủ điều kiện sau giảm giá và đưa giao dịch chênh lệch vào hàng đợi đối soát. | Kế toán trưởng |

## Rà soát trước khi chốt CP3

- [ ] Hai bộ nhãn gốc có đủ ca 1–20 và được giữ nguyên sau khi đối chiếu.
- [ ] Cột “Trùng?” so hai bộ nhãn gốc. Tỉ lệ đồng thuận từ 80% khi có ít nhất 16 ca trùng. Nếu thấp hơn, ghi định nghĩa đã chỉnh ở mục quy tắc phân biệt.
- [ ] Cột “Nhãn thống nhất” có đủ 20 ca. Mỗi ca bất đồng có một câu giải thích cách phân biệt.
- [ ] Năm ca khắc phục đại diện cho đủ năm loại theo nhãn đã thống nhất. Mỗi dòng có dấu hiệu đo được, cách xử lý và một vai trò chịu trách nhiệm.
- [ ] Khi có đáp án của giảng viên, đối chiếu nhãn thống nhất với đáp án theo ngưỡng 16/20 của rubric. Đây là phép kiểm tra riêng với tỉ lệ đồng thuận của hai người.

## Phân tích tham khảo

Xem [bảng đối chiếu tham khảo](../../docs/CP3_doi_chieu_tham_khao.md) để xem kết quả so sánh từng ca với phiếu Dũng.

Chỉ mở sau khi cả hai đã ghi xong bộ nhãn độc lập. Phần này dựa trên tình huống trong đề và [nhãn tham khảo trong hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca). Cột nhãn gốc và tỉ lệ đồng thuận sử dụng kết quả thực tế của hai thành viên.

<details>
<summary>Xem 20 nhãn tham khảo và kết quả đối chiếu với phiếu Dũng</summary>

Đối chiếu theo mã ca giữa phiếu Dũng (commit `97505fa`) và bảng tham khảo cho kết quả 20/20 ca trùng (100%). Tỉ lệ đồng thuận giữa Quốc và Dũng đang chờ phiếu riêng của Quốc.

| Ca | Nhãn tham khảo | Lý do |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu hai chữ số tài khoản. |
| 2 | Hệ thống | Trợ lý truyền loại hàng thường cho kiện hàng nặng, dẫn đến hoàn thiếu. |
| 3 | Ngữ cảnh | Tiền về ví theo thiết kế, còn khách chờ tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | LogiX thiếu dữ liệu về chặng do hãng nước ngoài giao. |
| 5 | Ngầm | Hoàn theo giá trước giảm và chỉ phát hiện khi kiểm tra mẫu. |
| 6 | Do người dùng | Khách chọn luồng giao trễ cho yêu cầu về hàng vỡ. |
| 7 | Hệ thống | Trợ lý báo thành công dù sổ cái chưa xác nhận giao dịch. |
| 8 | Hệ thống | Trợ lý dẫn một điều khoản không có trong chính sách hiện hành. |
| 9 | Do người dùng | Khách đưa mã đơn sàn thay vì mã vận đơn. |
| 10 | Ngữ cảnh | Quyết định đúng điều khoản bất khả kháng, trong khi ứng dụng vẫn tạo kỳ vọng giao trong 24 giờ. |
| 11 | Giới hạn hệ thống | Trợ lý chưa hỗ trợ xử lý âm thanh. |
| 12 | Ngầm | Kết quả đúng, nhưng chi phí token bất thường kéo dài mà chưa được phát hiện. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm đối tác nằm ngoài phạm vi trợ lý. |
| 14 | Do người dùng | Khách bấm xác nhận đã nhận tiền trước khi thực nhận. |
| 15 | Hệ thống | Tính sai tỉ lệ hoàn theo chính sách và bị phát hiện khi nhân viên xem lại. |
| 16 | Ngữ cảnh | Gửi ngay đúng thiết kế nhưng thời điểm gửi gây phiền cho khách. |
| 17 | Ngầm | Bảng giá lưu trong bộ nhớ đệm đã cũ, khoản lệch nhỏ kéo dài và không có ca mở lại. |
| 18 | Ngữ cảnh | Số tiền đúng, nhưng thông báo thiếu cách tính nên khách hiểu khác. |
| 19 | Giới hạn hệ thống | Đơn nằm ngoài thời hạn dữ liệu mà trợ lý truy cập được. |
| 20 | Hệ thống | Thiếu cơ chế chống trùng nên cùng một khoản được hoàn hai lần. |

</details>

## CP3 – Lượt bổ sung

**Trạng thái: Đang chờ hướng dẫn của giảng viên.** Tính đến 25/11/2026, repo chưa có văn bản hướng dẫn mới và chưa có bộ ca mới nào được chấp thuận cho lượt bổ sung. Vì vậy chưa thể lập hai phiếu trắng, chưa có nhãn để đối chiếu và chưa tính được tỉ lệ đồng thuận. Hai phiếu cũ và kết quả 20/20 trong mục “Đối chiếu tham khảo” ở trên được giữ nguyên.

| Hạng mục | Trạng thái | Ghi chú |
| --- | --- | --- |
| Hướng dẫn của giảng viên | Chưa có | Không thấy văn bản hướng dẫn mới trong repo |
| Bộ ca mới được chấp thuận | Chưa có | Chưa thấy văn bản chấp thuận bộ ca mới; bộ 20 ca hiện có là đề gốc Lab 13, chưa được xác nhận dùng cho lượt bổ sung |
| Phiếu trắng của Quốc | Chưa tạo | Chờ mã ca và nguyên văn tình huống được duyệt |
| Phiếu trắng của Dũng | Chưa tạo | Chờ mã ca và nguyên văn tình huống được duyệt |
| Bảng đối chiếu | Chưa có | Chỉ mở khi cả hai đã gửi bản hoàn tất |
| Số ca hợp lệ | Chưa xác định | Chưa có bộ ca được duyệt |
| Số ca trùng / tỉ lệ đồng thuận | Chưa tính | Sẽ giữ nguyên tỉ lệ tính trước thảo luận nếu sau này có đối chiếu |
| Ca còn chờ hai người chốt | Chưa có danh sách | Phát sinh sau khi ghép hai phiếu |
| Mức khớp đáp án giảng viên | Chưa tính | Chỉ tính khi có đáp án chính thức; kết quả 20/20 ở mục tham khảo không phải đáp án chính thức |

**Tin nhắn xin bộ ca hoặc phương án đánh giá thay thế:** [docs/CP3_luot_bo_sung_tin_nhan.md](../../docs/CP3_luot_bo_sung_tin_nhan.md).

**Điều kiện mở lại lượt bổ sung:** giảng viên gửi bộ ca mới hoặc chấp thuận phương án thay thế. Sau đó nhóm tạo hai phiếu trắng giống nhau, mỗi phiếu có mã ca, nguyên văn tình huống và ô “Nhãn của tôi”; chỉ liệt kê năm nhãn hợp lệ, không điền sẵn nhãn, không gợi ý riêng và không để người này xem lựa chọn của người kia. Chỉ bắt đầu đối chiếu khi cả hai đã gửi bản hoàn tất; giữ nguyên từng bản gốc và tỉ lệ đồng thuận tính trước thảo luận.
