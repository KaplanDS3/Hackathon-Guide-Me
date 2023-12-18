import no_boom_shelter
import yes_boom_shelter
import no_alert
import audio


def main():
    alarm = True
    hasBoomShelter = False
    if not alarm:
        audio.no_red_alart()
        no_alert.no_alert().run()
    else:
        if hasBoomShelter:
            audio.red_alart_area()
            yes_boom_shelter.yes_boom_shelter().run()
        else:
            audio.no_shelter_around()
            no_boom_shelter.noBoomShelter().run()


if __name__ == '__main__':
    main()
