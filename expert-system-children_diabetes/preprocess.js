const fun = () => {
    let list = document.getElementsByTagName("input");
    list.shift();
    list.shift();

    list.map(el => {
        el.value = el.value == "on" ? "True" : el.value == "" ? "False" : el.value;
        console.log("changed\n")
    })
}