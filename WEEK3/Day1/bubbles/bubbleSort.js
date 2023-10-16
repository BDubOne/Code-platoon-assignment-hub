// var sequence = [4, 3, 5, 0, 1]
// var swaps = 0

const arrayLength = 10;
const maxRandomValue = 10

const randomArray = Array.from({length: arrayLength }, () => Math.floor(Math.random() * maxRandomValue) + 1);

console.log(randomArray)

const bubblesort = (arr) => {
    let n = arr.length;
    let swaps = 0;

    for (let i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            [arr[i], arr[i +1]] = [arr[i + 1], arr[i]]
            swaps += 1
        } 
    }
    console.log("swaps = " + swaps)
    return arr

}
const blowingBubbles = bubblesort(randomArray)
console.log("blowing bubbles: " + blowingBubbles)

// const bigBubbleSort = (arr) => {
//     let n = arr.length;
//     let swapped;
//     let swaps = 0;
//     do {
//         swapped = false;
//         for (let i = 0; i < n - 1; i++) {
//             if (arr[i] > arr[i + 1]) {
//                 [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
//                 swapped = true;
//                 swaps += 1
//             }
//         } 
//         n--;
//     } while (swapped);
//     console.log("Swaps: " + swaps)
//     return arr;

// }

// const sortedArr = bigBubbleSort(randomArray);
// console.log("Sorted Array:", sortedArr);


