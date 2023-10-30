# Using ES Modules and importing / exporting

## Assignment Description

You will refactor this codebase to use ES Modules. You will also practice writing some tests, installing an npm module, and adding a small feature to your project, to get more practice with importing/exporting.

## Instructions

### Prerequesites

You must have node.js and npm installed.

### Tasks

#### Use ES Modules in your project

1. Update your `package.json` so that your [node.js project uses ES Modules](https://nodejs.org/api/esm.html). **Do not use the `.mjs` file extension for any files.**

2. Refactor the exising code to use ES Module imports / exports instead of the CommonJS imports / exports they are currently using.

**IMPORTANT:** As of 2023, Jest does not support ES Modules out-of-the-box. To get your tests to run wth ES Modules you will have to do a couple things. This is a common issue with JS projects - the JS ecosystem is not as standardized as, say, Python.


**First, get ES Modules working with `app.js` and the files it imports - get your program running. Then do this.**

1. Add "type": "module" to package.json (you may have already done this)

2. Update the test script in package.json to **exactly** this:

```javascript
"scripts": {
  "test": "node --experimental-vm-modules ./node_modules/.bin/jest"
}
```

3. In your project root directory, Create a jest.config.js file with exactly the following content:


```javascript
export default { transform: {} }
```

**You will still need to change the test file to do ES Module imports.** But now your tests should run once you do.

Sources: [This stack overflow post](https://stackoverflow.com/a/69059786/22371523) and [the jest docs](https://jestjs.io/docs/ecmascript-modules). The stack overflow post is easier to understand.

#### Write tests for `createCustomer()`

1. Add a test in a file named `customer.test.js` that tests `createCustomer` to confirm it returns an object with a `name` property and an `id` property which is not an empty string and contains a valid UUID. Read the [UUID github README](https://github.com/uuidjs/uuid#readme) docs to see how to do this.

> Stretch goal: Update `createCustomer()` so it returns `false` if `name` is an empty string. Add a test for this.

#### Add a `createdAt` property to the customer

1. Install the [date-fns](https://github.com/date-fns/date-fns) npm module.

2. Add a test for `createCustomer` that confirms it returns an object which has the property `createdAt`. *We haven't implemented the feature yet so this test will fail.*

3. Update `createCustomer()` so it returns an object with a `createdAt` property. For now, just hardcode this to "hello". `createCustomer()` should return something like this:

```json
{
  name: 'alice',
  id: 'f623c358-ec00-445d-adc3-28aa74029991',
  createdAt: 'hello'
}
```

Your tests should now pass.

4. Update the test to check if `customer.createdAt` is a valid date. Use the [date-fns parseISO](https://date-fns.org/v2.30.0/docs/parseISO) function to parse the `createdAt` datetime string into a Date and then use the [date-fns isValid](https://date-fns.org/v2.30.0/docs/isValid) function to check it. See [this article](https://geekflare.com/javascript-date-fns/). *We haven't implemented the feature yet so this test will fail.*

5. Update `createCustomer()` so that `createdAt` is now today's date in an ISO datetime string. See [the date-fns formatISO function docs](https://date-fns.org/v2.30.0/docs/formatISO). `createCustomer()` should return something like this:

```json
{
  name: 'alice',
  id: 'f623c358-ec00-445d-adc3-28aa74029991',
  createdAt: '2023-10-27T15:03:53-05:00',
}
```

Your tests should now pass.
