async function analyzeResume(){
const resume=document.getElementById("resume").value.trim();
const job=document.getElementById("job").value.trim();
const btn=document.getElementById("analyzeBtn");
const status=document.getElementById("status");
const box=document.getElementById("resultBox");
status.textContent=""; box.classList.add("hidden");
if(!resume||!job){status.textContent="Please fill in both fields.";return;}
btn.disabled=true;btn.textContent="Analyzing...";
try{
const r=await fetch("/analyze",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({resume,job})});
const data=await r.json();
if(!r.ok)throw new Error(data.error||"Something went wrong.");
document.getElementById("result").textContent=data.result;
box.classList.remove("hidden");
}catch(e){status.textContent=e.message}
finally{btn.disabled=false;btn.textContent="Analyze with AI";}
}
function copyResult(){navigator.clipboard.writeText(document.getElementById("result").textContent)}