# Ví dụ kiểm thử tự động sử dụng CodeCept và REST helper

Ứng dụng ví dụ được viết bằng [Sanic framework](https://github.com/huge-success/sanic)
quản lý việc thêm, tìm kiếm, đổi password của user

## Cài đặt không dùng Docker
Chú ý việc cài đặt Sanic trên Windows tương đối khó khăn. Nếu dùng Windows bạn nên chuyển sang cài đặt bằng Docker
Clone repo này và sau đó chạy file main.py để dựng REST server thử nghiệm lắng nghe ở cổng 8000

```shell
$ git clone https://github.com/TechMaster/automation_test_rest.git
$ cd automation_test_rest
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```
Thử mở browser rồi truy cập vào http://localhost:8000/users xem danh sách users trả về

## Cài đặt sử dụng Docker
Hãy cài đặt Docker trên máy tính của bạn
Mở terminal hoặc Powershell (windows), chạy lệnh ```docker-compose up -d```

```shell
$ git clone https://github.com/TechMaster/automation_test_rest.git
$ cd automation_test_rest
$ docker-compose up -d
```
Mở browser rồi truy cập vào http://localhost:8000/users xem danh sách users trả về



## Kiểm thử

Tạo mới một màn hình hay tab terminal, cài đặt phần mềm cần thiết cho CodeCept chạy
```shell
$ cd automation_test_rest\test
$ npm install
```

Giờ thì chạy lệnh để kiểm thử, đảm bảo bạn đang ở thư mục automation_test_rest\test
```shell
$ npx codeceptjs run --verbose
```

## Cấu hình
Toàn bộ phần unit test chỉ cần module codecept
```json
  "devDependencies": {
    "codeceptjs": "^2.3.5"
  },
```

Hãy để ý đến file cấu hình codecept.conf.js, phần helpers chỉ cần REST và ghi rõ endpoint là đủ, không cần các helper khác vì chúng ta tập trung kiểm thử REST
```json
exports.config = {
  tests: './*_test.js',
  helpers: {
    REST: {
      endpoint: 'http://localhost:8000'
   }
  },
  include: {
    I: './steps_file.js'
  },
  bootstrap: null,
  name: 'webtest'  
}
```

### Các file test để ở đâu?

1. Các file kiểm thử luôn có đuôi _test.js. Quy ước được định ở thuộc tính test trong file codecept.conf.js
```json
tests: './*_test.js',
```

2. Chúng ta nên đánh số thứ tự chạy bằng số 01, 02, 03. Ví dụ:
  - 01_basic_test.js
  - 02_advanced_test.js
  - 03_getuser_test.js