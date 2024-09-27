Bài tập Odoo - Mở rộng quản lý Employee (Nâng cao)
Mục tiêu: Tạo một module Odoo mới để mở rộng tính năng cho ứng dụng Employee, với mức độ yêu cầu cao hơn bao gồm: kế thừa model phức tạp, tạo wizard với logic phức tạp, phân quyền nâng cao, kế thừa quyền và view một cách tối ưu, thêm smartbutton với xử lý dữ liệu, và xử lý các hành động trên record với các ràng buộc và xử lý phức tạp.

Chi tiết yêu cầu từng phần:
1. Kế thừa Model Employee (Nâng cao)
· Mô tả: Kế thừa model hr.employee để thêm nhiều trường mới. Ví dụ:
o years_of_experience (số năm kinh nghiệm).
o certifications (chứng chỉ) là một bảng liên kết chứa thông tin về các chứng chỉ mà nhân viên đã đạt được.
o skills (kỹ năng) là một bảng liên kết chứa các kỹ năng của nhân viên, mỗi kỹ năng có điểm số đánh giá.
· Điểm đánh giá: 15 điểm.
· Yêu cầu:
o Kế thừa model hr.employee để thêm các trường phức tạp. (done)
o Bảng liên kết certifications và skills phải có mối quan hệ rõ ràng với hr.employee.  (done)
o Tạo các phương thức xử lý cho bảng liên kết này, chẳng hạn như tự động cập nhật years_of_experience dựa trên chứng chỉ hoặc kỹ năng. ( done )
2. Tạo Wizard với Logic Phức Tạp
· Mô tả: Tạo một wizard phức tạp để cập nhật các thông tin như kinh nghiệm, chứng chỉ, kỹ năng của nhiều nhân viên cùng lúc. Wizard phải cho phép lựa chọn nhiều nhóm nhân viên và cập nhật nhiều trường dữ liệu cùng một lúc với logic phức tạp (ví dụ: chỉ cập nhật nếu nhân viên thuộc một bộ phận nhất định hoặc nếu họ đã làm việc đủ thời gian).
· Điểm đánh giá: 25 điểm.
· Yêu cầu:
o Tạo wizard cho phép người dùng chọn nhiều nhóm nhân viên (dựa trên bộ phận, chức vụ, số năm kinh nghiệm, v.v.)	.(done)
o Wizard phải có khả năng cập nhật nhiều trường dữ liệu cùng lúc, ví dụ: thêm chứng chỉ, cập nhật kỹ năng. 	(done)
o Logic xử lý phức tạp: chỉ cập nhật dữ liệu nếu thỏa mãn các điều kiện cụ thể (ví dụ: chỉ nhân viên có kinh nghiệm > 5 năm mới được cập nhật).	
done
3. Phân quyền nâng cao	( done)
· Mô tả: Tạo một hệ thống quyền phân tầng cho phép quản lý các quyền riêng biệt trên các trường dữ liệu mới. Ví dụ: quyền quản lý kỹ năng chỉ thuộc về một nhóm nhất định, quyền quản lý chứng chỉ thuộc về nhóm khác.
· Điểm đánh giá: 15 điểm.
· Yêu cầu:
o Tạo các nhóm quyền riêng biệt cho các chức năng khác nhau (ví dụ: quản lý chứng chỉ, quản lý kỹ năng).
o Đảm bảo rằng các quyền được phân tách rõ ràng và người dùng chỉ có thể truy cập những gì họ được phép.
o Cấu hình các quyền truy cập trong ir.model.access.csv và các quy tắc bảo mật trong security.xml.
4. Kế thừa Quyền (Nâng cao)	( chưa xử lý)
· Mô tả: Kế thừa quyền của nhóm "Employee Experience Manager" để mở rộng quyền truy cập vào các thông tin khác trong employee, nhưng áp dụng thêm các quy tắc điều kiện cho quyền đó (ví dụ: chỉ được phép cập nhật kỹ năng nếu nhân viên đã hoàn thành một số chứng chỉ nhất định).
· Điểm đánh giá: 10 điểm.
· Yêu cầu:
o Kế thừa quyền của nhóm "Employee Experience Manager" và thêm điều kiện phức tạp cho quyền truy cập (ví dụ: quyền chỉ được kích hoạt khi nhân viên thỏa mãn điều kiện nào đó).
o Cấu hình các quy tắc bảo mật nâng cao, sử dụng các điều kiện lọc.
5. Kế thừa View (Nâng cao)		(done )
· Mô tả: Kế thừa form view của hr.employee để hiển thị các trường mới như certifications, skills, nhưng với điều kiện hiển thị dựa trên quyền hoặc điều kiện logic (ví dụ: chỉ hiển thị skills nếu nhân viên có ít nhất một chứng chỉ).
· Điểm đánh giá: 15 điểm.
· Yêu cầu:
o Kế thừa form view và thêm điều kiện hiển thị dựa trên quyền hoặc giá trị của các trường khác (ví dụ: nếu nhân viên có chứng chỉ mới được hiển thị trường kỹ năng).
o Sử dụng các điều kiện attrs, invisible, readonly trong view một cách hợp lý để tạo ra trải nghiệm người dùng tốt.
6. Thêm Smartbutton với Xử Lý Phức Tạp	 (done))
· Mô tả: Thêm một smartbutton vào form view của employee để thực hiện các hành động liên quan đến kỹ năng và chứng chỉ. Ví dụ: nút smartbutton sẽ mở wizard hoặc trigger một hành động tự động cập nhật kỹ năng dựa trên các chứng chỉ đã đạt được.
· Điểm đánh giá: 10 điểm.
· Yêu cầu:
o Thêm smartbutton với biểu tượng và chức năng rõ ràng, thực hiện hành động cụ thể (ví dụ: mở wizard cập nhật kỹ năng dựa trên chứng chỉ).
o Smartbutton phải tích hợp logic xử lý dữ liệu (ví dụ: cập nhật tự động hoặc đưa ra cảnh báo nếu dữ liệu không phù hợp).
7. Xử Lý Record với Ràng Buộc Phức Tạp	 (chưa xử lý)
· Mô tả: Xử lý các record của employee với các ràng buộc phức tạp. Ví dụ: khi nhân viên đạt được một chứng chỉ mới, hệ thống tự động tính toán lại kỹ năng và cập nhật years_of_experience tương ứng. Nếu không đạt yêu cầu (ví dụ: kỹ năng vượt quá giới hạn), hệ thống đưa ra cảnh báo và rollback hành động.
· Điểm đánh giá: 20 điểm.
· Yêu cầu:
o Kế thừa phương thức write và create để xử lý các ràng buộc phức tạp trên dữ liệu (ví dụ: tự động cập nhật kỹ năng khi chứng chỉ được thêm mới).
o Sử dụng các cơ chế kiểm tra dữ liệu và rollback (hoặc đưa ra cảnh báo) nếu dữ liệu không phù hợp (ví dụ: số kỹ năng vượt quá giới hạn cho phép).

Tổng Kết
· Điểm tối đa: 110 điểm (bài tập khó hơn tiêu chuẩn).
· Phân bổ điểm:
o Kế thừa Model (Nâng cao): 15 điểm
o Wizard với Logic Phức Tạp: 25 điểm
o Phân quyền nâng cao: 15 điểm
o Kế thừa quyền (Nâng cao): 10 điểm
o Kế thừa view (Nâng cao): 15 điểm
o Smartbutton với xử lý phức tạp: 10 điểm
o Xử lý record với ràng buộc phức tạp: 20 điểm
Lưu ý: Đảm bảo triển khai đầy đủ các yêu cầu nâng cao và nộp lại module để đánh giá chi tiết từng phần.
 

