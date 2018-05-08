from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.StrictRedis(host='192.168.7.103', port=6379)


@app.route("/")
def hello():
    r.pfadd("Unique-User-Agent", request.user_agent.string)
    return str(r.pfcount("Unique-User-Agent"))


def main():
    app.run()


if __name__ == '__main__':
    main()
