
function openPreview() {
    document.getElementById("res-name").innerText = document.getElementById("name").value;
    document.getElementById("res-email").innerText = document.getElementById("email").value;
    document.getElementById("res-phone").innerText = document.getElementById("phone").value;
    document.getElementById("res-linkedin").innerText = document.getElementById("linkedin").value;
    document.getElementById("res-education").innerText = document.getElementById("education").value;
    document.getElementById("res-experience").innerText = document.getElementById("experience").value;
    document.getElementById("res-skills").innerText = document.getElementById("skills").value;

    document.getElementById("resumePopup").style.display = "block";
}

function closePreview() {
    document.getElementById("resumePopup").style.display = "none";
}

function downloadPDF() {
const { jsPDF } = window.jspdf;
const pdf = new jsPDF();

// Set Title
pdf.setFont("helvetica", "bold");
pdf.setFontSize(18);
pdf.setTextColor(255, 255, 255);
pdf.setFillColor(0, 123, 255);
pdf.rect(10, 10, 190, 10, "F");
pdf.text("Resume", 90, 17);

pdf.setFontSize(12);
pdf.setTextColor(0, 0, 0);

function addBoxedText(title, content, yPos) {
pdf.setFillColor(230, 242, 255);
pdf.rect(10, yPos, 190, 10, "F");

pdf.setFont("helvetica", "bold");
pdf.text(title + ":", 15, yPos + 7);

pdf.setFont("helvetica", "normal");
pdf.text(content, 15, yPos + 17);

return yPos + 25;
}

let y = 30;
y = addBoxedText("Name", document.getElementById("name").value, y);
y = addBoxedText("Email", document.getElementById("email").value, y);
y = addBoxedText("Phone", document.getElementById("phone").value, y);
y = addBoxedText("LinkedIn", document.getElementById("linkedin").value, y);
y = addBoxedText("Education", document.getElementById("education").value, y);
y = addBoxedText("Work Experience", document.getElementById("experience").value, y);
y = addBoxedText("Skills", document.getElementById("skills").value, y);

pdf.save("Resume.pdf");
}

