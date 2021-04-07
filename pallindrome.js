// Create a function that returns a boolean whether the string is a strict palindrome. 
// For "a x a" or "racecar", return true. 
// Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.

function palindrome(str) {
    var temp = str;
    var array = str.split("");
    array = array.reverse();
    array= array.join("");
    console.log(array)
    if(array == temp){
        return(true);
    }
        else {
            return(false);
        }
    }

console.log(palindrome("gooG"));
