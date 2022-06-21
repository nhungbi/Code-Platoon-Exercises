const findShiftedChar = (char, shiftAmount) => {
    const charValue = char.charCodeAt() - 96
    let newValue = (charValue + shiftAmount) % 26

    if (newValue === 0) {
        newValue = 26
    } else if (newValue < 0) {
        newValue += 26}
        
    return String.fromCharCode(newValue + 96)
}

exports.caesarCipher = function(str, shiftAmount) {
    let shiftedString= ''
    for (let char of str) {
        if (char.match(/[a-z]/)) {
            const newChar = findShiftedChar(char, shiftAmount)
            shiftedString += newChar
        } else if (char.match(/[A-Z]/)) {
            shiftedString += findShiftedChar(char.toLowerCase(), shiftAmount).toUpperCase()
        } else {
            shiftedString += char
        }
    }
    return shiftedString
};

//console.log(String.fromCharCode(97)) = 'a' so 1 + 96
//console.log('a'.charCodeAt()) = 97, so -97, -96 to get 1
// console.log(exports.caesarCipher("Boy! What a string!", -5))
// console.log(findShiftedChar('b', -5))