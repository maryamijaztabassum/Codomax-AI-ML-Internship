const task = document.getElementById("task");
const inputText = document.getElementById("inputText");
const result = document.getElementById("result");
const generateBtn = document.getElementById("generateBtn");
const copyBtn = document.getElementById("copyBtn");

generateBtn.addEventListener("click", async () => {
    const text = inputText.value.trim();

    if (!text) {
        result.textContent = "Please enter some text or an idea first.";
        return;
    }

    generateBtn.disabled = true;
    generateBtn.textContent = "Working...";
    result.textContent = "Generating your result...";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                task: task.value,
                text: text
            })
        });

        const data = await response.json();
        result.textContent = data.result || data.error || "No result returned.";
    } catch (error) {
        result.textContent = "Something went wrong. Please try again.";
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = "Run AI Assistant";
    }
});

copyBtn.addEventListener("click", async () => {
    await navigator.clipboard.writeText(result.textContent);
    copyBtn.textContent = "Copied";
    setTimeout(() => copyBtn.textContent = "Copy", 1200);
});
