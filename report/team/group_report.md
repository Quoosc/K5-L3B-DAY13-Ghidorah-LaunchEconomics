# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Ghidorah
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí, mức sử dụng và rủi ro của trợ lý hoàn phí LogiX-VN để đề xuất một pilot có đối chứng. Dữ liệu chạy thử gồm 1.200 yêu cầu giả lập.

## 3. Giải pháp

- A/B dùng trace và dữ liệu yêu cầu để tính chi phí, so với nhân viên tự làm và phân tích độ nhạy. Kết quả đã được đối chiếu với code chạy trên hai CSV. Chi tiết ở [bảng chi phí](bang_chi_phi.md).
- C phân loại theo nguyên nhân gốc. Đã có phần tham khảo 20 ca và năm đề xuất khắc phục. Bảng CP3 ghi từng nhãn của Dũng (phiếu gốc ở commit `97505fa`) cạnh nhãn Codex lập theo ủy quyền. Hai nguồn khớp 20/20 mã ca. Sau khi Quốc hoàn tất phiếu riêng, hai người ghi kết quả đối chiếu trong [bảng lỗi](bang_loi.md).
- D đề xuất ngẫu nhiên theo nhân viên với đối chứng chạy cùng thời gian. Xem [kế hoạch pilot](pilot_plan.yaml).
- E tính chỉ số từ CSV và thiết kế sự kiện để đo trong pilot. Xem [chỉ số](chi_so.md) và [hồ sơ launch](ho_so_launch_v0.md).

## 4. Kết quả

Chi phí mỗi việc thành công là 4.472 đ [simulated]. Giới hạn 2 lần chạy cho chi phí cả hệ thống khoảng 5.751 đ/yêu cầu [simulated], so với mốc 12.000 đ tự làm. Làm lại gấp đôi làm chi phí mỗi việc thành công tăng 51,8% [simulated].

Đợt thử có 994/1.200 yêu cầu đạt chỉ số chính (82,83%), 48/177 yêu cầu được xem lại có sửa hoặc bỏ gợi ý (27,12%) và 51/1.200 yêu cầu mở lại trong 7 ngày (4,25%). Đề xuất hiện tại là No-go cho đến khi đủ bằng chứng. Chưa có kết quả duyệt chéo.

## 5. Khó khăn và cách xử lý

Mẫu lịch sử có 20 nhân viên tại 6 depot. Trước khi trình pilot, Giám đốc vận hành cần xác nhận 40 nhân viên đủ điều kiện, danh sách phân nhánh và dự báo đủ 299 yêu cầu mỗi người. Nếu thiếu người hoặc sản lượng, nhóm cần tính lại cỡ mẫu.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Chạy thử thiếu đối chứng nên chỉ số quan sát chưa cho biết tác động của trợ lý. Phương án ngẫu nhiên theo nhân viên cần 299 yêu cầu mỗi người và đủ 20 người mỗi nhánh để nhận biết chênh lệch 6 điểm theo giả định của đề.

## 8. Tài liệu tham khảo

- [Đề bài Lab 13](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx)
- [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md)
- [Rubric](../../RUBRIC.md)
