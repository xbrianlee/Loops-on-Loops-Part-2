// Merge sort
function merge(left, right) {
    var result = [];
    var left_itor = 0;
    var right_itor = 0;
    while (left_itor < left.length && right_itor < right.length) {
        if (left[left_itor] < right[right_itor]) {
            result.push(left[left_itor++]);
        }else {
            result.push(right[right_itor++]);
        }
     }
     return result.concat(left.slice(left_itor)).
                   concat(right.slice(right_itor));
}


function mergeSort(array) {
    if (array.length < 2) {
        return array;
    }

    var mid = Math.floor(array.length / 2);
    var left = array.slice(0, mid); 
    var right = array.slice(mid);

    return merge(mergeSort(left), mergeSort(right));
}

var array = [5, 4, 2, 3, 6, 1];
var sorted = mergeSort(array);
for(var i = 0; i < array.length; ++i) {
    console.log(sorted[i]);
}
