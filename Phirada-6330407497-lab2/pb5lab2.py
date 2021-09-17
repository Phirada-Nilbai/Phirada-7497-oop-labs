#Phirada Nilbai 633040749-7
taekwondo_olympics2020_w49k = {'Gold': {'Thailand'}}
taekwondo_olympics2020_w49k2 = {'Silver': {'Spain'}, 'Bronze': {'Israel', 'Serbia'}}
taekwondo_olympics2020_w49k.update(taekwondo_olympics2020_w49k2)

if __name__ == '__main__':
    s = {}
    s['Gold'] = "Thailand"
    s['Silver'] = "Spain"
    s['Bronze'] = "Israel"

    print("The list of medals in Taekwondo Olympics 2020 women 49 kilograms:")

    for item in s:
        print("{} received {} medal".format(s[item], item))
        if item == 'Bronze':
            s['Bronze'] = "Serbia"
            print("{} received {} medal".format(s[item], item))

    print("The dictionary of medal is", taekwondo_olympics2020_w49k)
