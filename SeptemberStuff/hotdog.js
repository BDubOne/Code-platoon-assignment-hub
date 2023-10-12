function hotdogCommander(hotDogs) {

    if (hotDogs < 3) {
        hotDogs += 5;
        hotdogCommander(hotDogs);
    }else if (hotDogs > 5) {
        console.log ("That's plenty of hotdogs")
    }
    return hotDogs
    }

    console.log(hotdogCommander(1))
