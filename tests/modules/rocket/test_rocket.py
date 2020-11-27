from tests.modules.rocket.rocket import getRocket


def testRocketModel():
    rocket = getRocket()
    rocket.setCalculatedParameters(cg=300)
    print(rocket.cn_alpha)
    print(rocket.cm_alpha)


if __name__ == '__main__':
    testRocketModel()
