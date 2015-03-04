var script = document.createElement('script');
script.src = 'http://code.jquery.com/jquery-1.11.0.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);


// Merge sort
function merge(left, right, arr) {
    var a = 0;
    while (left.length && right.length)
        arr[a++] = right[0] < left[0] ? right.shift() : left.shift();
    while (left.length) arr[a++] = left.shift();
    while (right.length) arr[a++] = right.shift();
}

function sort(arr, tmp, len) {
    if (len == 1) return;
    var     m = Math.floor(len / 2),
        tmp_l = tmp.slice(0, m),
        tmp_r = tmp.slice(m);
    sort(tmp_l, arr.slice(0, m), m);
    sort(tmp_r, arr.slice(m), len - m);
    merge(tmp_l, tmp_r, arr);
}

function mergeSort(arr) {
    sort(arr, arr.slice(), arr.length);
}

/*// Merge sort
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

function mergeSort(arr) {
    if (arr.length < 2) {
        return arr;
    }

    var mid = Math.floor(arr.length / 2);
    var left = arr.slice(0, mid); 
    var right = arr.slice(mid);

    return merge(mergeSort(left), mergeSort(right));
} */

// Quick sort
function swap(items, firstIndex, secondIndex){
    var temp = items[firstIndex];
    items[firstIndex] = items[secondIndex];
    items[secondIndex] = temp;
}

function partition(items, left, right) {

    var pivot   = items[Math.floor((right + left) / 2)],
        i = left,
        j = right;

    while (i <= j) {
        while (items[i] < pivot) {
            i++;
        }
        while (items[j] > pivot) {
            j--;
        }
        if (i <= j) {
            swap(items, i, j);
            i++;
            j--;
        }
    }
    return i;
}

function quickSort(items, left, right) {
    var index;
    if (items.length > 1) {
        index = partition(items, left, right);
        if (left < index - 1) {
            quickSort(items, left, index - 1);
        }
        if (index < right) {
            quickSort(items, index, right);
        }
    }
    return items;
}

// Bubble sort
function bubbleSort(arr)
{
    var swapped;
    do {
        swapped = false;
        for (var i=0; i < arr.length-1; i++) {
            if (arr[i] > arr[i+1]) {
                var temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                swapped = true;
            }
        }
    } while (swapped);
    return arr;
}

// Heap sort
function heapSort(arr) {
    heapify(arr, arr.length);
    end = arr.length - 1;
    while(end > 0) {
        swap(arr[end], arr[0]);
        --end;
        siftDown(arr, 0, end);
    }
    return arr;
}

function heapify(arr) {
    start = (arr.length - 2) / 2;

    while(start >= 0) {
        siftDown(arr, start, arr.length);
        --start;
    }
    return arr;
}

function siftDown(arr, start, end) {
    var root = start;
    var child;
    while(root * 2 + 1 <= end) {
        child = root * 2 + 1;
        if(child + 1 <= end && arr[child] < arr[child + 1]) {
            ++child;
        }
        if(arr[root] < arr[child]) {
            swap(arr[root], arr[child]);
            root = child;
        }else {
            return arr;
        }
    }
}


// Test speed for each sorting algorithm
function speedTest(arr) {
    // Merge sort speed test
    var start_merge_sort = performance.now();
    var merge_sorted = mergeSort(arr);
    var end_merge_sort = performance.now();
    var merge_time = end_merge_sort - start_merge_sort;

    // Quick sort speed test
    var start_quick_sort = performance.now();
    var quick_sorted = quickSort(arr);
    var end_quick_sort = performance.now();
    var quick_time = end_quick_sort - start_quick_sort;

    // Bubble sort speed test
    var start_bubble_sort = performance.now();
    var bubble_sorted = quickSort(arr);
    var end_bubble_sort = performance.now();
    var bubble_time = end_bubble_sort - start_bubble_sort;

    // Heap sort speed test
    var start_heap_sort = performance.now();
    var heap_sorted = quickSort(arr);
    var end_heap_sort = performance.now();
    var heap_time = end_heap_sort - start_heap_sort;

    console.log(merge_time);
    console.log(quick_time);
    console.log(bubble_time);
    console.log(heap_time);
}

function testInputFile(text) {
    var arr = [];
    for(var i = 0; i < text.length; ++i) {
        arr.push(text[i]);
    }
    speedTest(arr);
    
}
// Upload text file
document.getElementById('file').onchange = function() {
    var input_array = [];
    var file = this.files[0];

    var reader = new FileReader();
    reader.onload = function(progressEvent) {
        console.log(this.result);
        
        var lines = this.result.split('\n');
        var input_text = lines + '';
        for(var line = 0; line < lines.length; ++line) {
            console.log(lines[line]);
        }
        var split_txt = input_text.split(/[\s,.]+/);
        testInputFile(split_txt);

    };
    reader.readAsText(file);
}

