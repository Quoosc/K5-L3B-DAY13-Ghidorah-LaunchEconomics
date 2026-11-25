# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **4.472 ÷ 274,7 ≈ 16,3 lần** [simulated].
- Khoản lớn nhất là **làm lại: 2.264.000 đ, chiếm 51,8%**. Xem lại chiếm 40,7%. Tổng giờ nhân viên chiếm 92,5% chi phí [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- **quoc_te** có chi phí 22.515 đ/việc, bằng **1,88×** mốc 12.000 đ [simulated], và chỉ **27,3%** thành công. Tỉ lệ run ok giảm **30,0% → 11,4% → 2,2%** qua ba lượt. **doi_tac** cũng nằm ngoài phạm vi pilot đề xuất (10.215 đ/việc, 0,85× [simulated]).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Sau khi cộng chi phí cố định, chi phí là **4.599 đ = 0,38×** ở 45.000 yêu cầu/tháng và **5.784 đ = 0,48×** ở nửa khối lượng. Chi phí chạm mốc 12.000 đ/việc ở khoảng **6.200 yêu cầu/tháng** [simulated].

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi cho **6.543 đ/việc, +46,3%**. Mức tăng bằng tổng hai tác động riêng sau khi làm tròn (+5,6% và +40,7%) vì mô hình cộng tuyến tính [simulated].
- Ba yếu tố ảnh hưởng mạnh nhất là **làm lại** (+51,8% khi gấp đôi), **xem lại** (+40,7% khi gấp đôi) và **lương nhân viên** (+23,1% khi tăng 25%) [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn **2 lần** cho tổng chi phí hệ thống thấp nhất (**6.901.220 đ**), còn giới hạn **1 lần** cho chi phí mỗi việc thành công thấp nhất (**4.111 đ**) [simulated]. Giới hạn 1 lần có thêm **85 yêu cầu không thành công** so với 2 lần (319 so với 234).

## B4 · Nếu phải xem lại tất cả

- Khi xem lại cả 948 yêu cầu có ít nhất một run `ok` trong phạm vi `noi_dia` + `hang_nang`, chi phí là **11.743 đ/việc = 0,98×** [simulated]. Cộng 948 × 5 × 2.000 đ xem lại, 48 × 9 × 2.000 đ làm lại và 224.513 đ token + tool, rồi chia 900 việc thành công.
- Với kịch bản **15,3 phút/ca** làm lại, chi phí là **12.415 đ = 1,03×**. Dùng trung bình từ cột giả lập của 48 ca trong phạm vi (**16,25 phút/ca**) thì lên **12.516 đ = 1,04×** [simulated]. Pilot cần đo tỉ lệ và phút xem lại. Mốc hòa vốn khoảng **5,1 phút** mỗi lần xem lại nếu làm lại 9 phút, hoặc **4,8 phút** nếu làm lại 15,3 phút [simulated].
