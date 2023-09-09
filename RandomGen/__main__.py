import getopt
import sys

from RandomGen.random_number_generator import RandomGen

random_gen = RandomGen(
    [
        1,
    ],
    [
        1,
    ],
)


def main(argv):
    opts, args = getopt.getopt(argv, "hn:c", ["config=", "pmf"])
    observation_size = values = probs = None
    pmf = False
    for opt, arg in opts:
        if opt == "-h":
            print("Simple random number generator")
            sys.exit()
        elif opt == "-n":
            observation_size = int(arg)
        elif opt == "--config" or opt == "-c":
            print("values: ")
            values = list(map(int, input().split()))
            print("probabilities: ")
            probs = list(map(float, input().split()))
        elif opt == "--pmf":
            pmf = True

    print("output_size: ")
    output_size = int(input().strip(""))

    if observation_size:
        random_gen.resize(observation_size)
    if values and probs:
        random_gen.reinit(values, probs)
    random_gen.reinit(values, probs)

    if output_size > observation_size:
        raise ValueError("more outputs than observations")

    count = 0
    while output_size:
        output_size -= 1
        count += 1
        print(f"{count}: {next(random_gen)}")

    if pmf:
        random_gen.recount()
        print("probability mass function: ")
        print(random_gen.pmf)


if __name__ == "__main__":
    main(sys.argv[1:])
