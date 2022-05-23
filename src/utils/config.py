def db_cfg(path="./rsc/config.cfg"):
    with open(path, "r", encoding="cp949") as f:
        data = f.read()
        data = data.split("\n")
        data = [_.split("=") for _ in data]
        data = dict([(_[0], _[1]) for _ in data])
    return data


if __name__ == "__main__":
    db_cfg()
