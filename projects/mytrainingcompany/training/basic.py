training_example = ["Python essentiel", 5, [], 12, 2500]


def create_training(title, duration, price, seats=12):
    return [title, int(duration), [], int(seats), int(price)]


def add_trainee(training, name):
    _, _, trainees, seats, _ = training
    if len(trainees) >= seats:
        raise ValueError("Training full")  # Not the best error to be raised

    trainees.append(name)


def remove_trainee(training, name):
    trainees = training[2]

    trainees.remove(name)
