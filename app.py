from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 메인 페이지
@app.route("/")
def index():
    return render_template("index.html")


# 검사 결과 저장 (프론트에서 보내는 데이터 받기)
@app.route("/result", methods=["POST"])
def result():
    data = request.json

    # 여기서 DB 저장 or 로그 확인 가능
    print("검사 결과:", data)

    return jsonify({"status": "success"})


# 서버 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)