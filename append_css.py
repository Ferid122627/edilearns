import os

path = 'style.css'
with open(path, 'a', encoding='utf-8') as f:
    f.write('''
/* --- AGENT HUB UI --- */
.agent-hub-container {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
    flex-wrap: wrap;
}
.agent-card {
    flex: 1;
    min-width: 250px;
    background: var(--card-color);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-color);
    border-radius: var(--card-radius);
    padding: 20px;
    box-shadow: var(--shadow-sm);
    transition: var(--transition-normal);
}
.agent-card:hover {
    box-shadow: var(--shadow-glow);
    transform: translateY(-5px);
}
.agent-icon {
    font-size: 2.5rem;
    margin-bottom: 15px;
    display: inline-block;
}
.pulsing-blue { animation: pulse-glow 2s infinite; color: var(--primary-color); }
.pulsing-purple { animation: pulse-glow 2s infinite; animation-delay: 0.5s; color: var(--secondary-color); }
.pulsing-green { animation: pulse-glow 2s infinite; animation-delay: 1s; color: var(--success-color); }

.agent-log {
    background: #000;
    color: #0f0;
    font-family: monospace;
    padding: 10px;
    border-radius: 5px;
    margin-top: 15px;
    font-size: 0.85rem;
    height: 80px;
    overflow: hidden;
}
.agent-log p { margin: 2px 0; }
.blink { animation: blinker 1s linear infinite; }
@keyframes blinker { 50% { opacity: 0; } }

.status-scanning { color: var(--primary-color); font-weight: bold; }
.status-idle { color: var(--warning-color); font-weight: bold; }
.status-active { color: var(--success-color); font-weight: bold; }
''')
print("Appended Agent Hub CSS")
