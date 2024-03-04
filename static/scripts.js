function redirectToSelected(dropdownId) {
    let dropdown = document.getElementById(dropdownId);
    let selectedOption = dropdown.options[dropdown.selectedIndex].value;
    if (selectedOption !== "") {
        window.location.href = selectedOption;
    }
}
