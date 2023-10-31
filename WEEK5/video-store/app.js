import inventoryJson from './video-store-inventory.json' assert {type:"json"};
import { v4 as uuidv4 } from 'uuid';
import { format, parse } from 'date-fns'


const state = {
    customers: [],
    videos: []
}


const inventory = inventoryJson
.map(video => {
    const { id, ...rest } = video;
    return {
        imdbId: id,
        ...rest
    };
})
.map(video => {
    return {

        ...video,
        imdbId: uuidv4()
    };
})
.map(video => {
    return {
        ...video,
        _meta: {
            createdAt: format(new Date(), "yyyy-MM-dd'T'HH:mm:ss")
        }
    };
});

state.videos.push(...inventory)

console.log(state)

const makeCustomer = (state, name, email, checkoutOut = []) => {
    const customer = {
        cxId: uuidv4(),
        name: name,
        email: email,
        checkedOut: checkedOut
    };
    state.customers.push(customer)
    return customer

}


const getCustomerById = (state, cxId) => {
    result = state.customers
    .filter(customer => customer.cxId === cxId);
    return result
}

const findCustomerByEmail = (state, email) => {
    result = state.customers
    .filter(customer =>customer.email === email)
    return result[0]
}

const findCustomerByName = (state, name) => {
    result = state.customers
    .filter(customer => customer.name === name)
    return result
}

const findVideoByImdbId = (state,imdbId) => {
    result = state.videos
    .filter(video => video.imdbId === imdbId)
    return result[0]
}

const findVideoByTitle = (state, title) => {
    result = state.videos
    .filter(video => video.title === title)
    return result
}

console.log(findVideoByTitle("Creed III"))



