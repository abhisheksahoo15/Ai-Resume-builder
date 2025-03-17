function updatePreview() {
    ["name", "email", "phone", "linkedin", "education", "experience", "projects", "certifications"]
    .forEach(field => document.getElementById(`res-${field}`).innerText = document.getElementById(field).value || `Your ${field}`);
}

function downloadPDF() {
    const { jsPDF } = window.jspdf;
    html2canvas(document.getElementById("resume"), { backgroundColor: "#ffffff" }).then(canvas => {
        let imgData = canvas.toDataURL("image/png");
        let doc = new jsPDF("p", "mm", "a4");

 
        let imgWidth = 200; 
        let imgHeight = (canvas.height * imgWidth) / canvas.width;
        doc.addImage(imgData, "PNG", 8, 8, imgWidth - 6, imgHeight - 6);
        doc.save("resume.pdf");
    });
}