import os

def fix_and_inject(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix broken function calls
    content = content.replace('showAgent HubPanel', 'showEduBotPanel')
    content = content.replace('Agent Hub-a', 'Agent Hub')

    # Agent Hub Injection HTML
    agent_hub_html = '''
    <main id="edubot-panel" class="edubot-area hidden">
        <h2 class="content-section-header">Agent Hub: Autonomous Core</h2>
        <div class="agent-hub-container">
            <div class="agent-card">
                <div class="agent-icon pulsing-blue">🤖</div>
                <h3>Tutor Agent</h3>
                <p>Status: <span class="status-scanning">Scanning for resources...</span></p>
                <div class="agent-log">
                    <p>> Querying Khan Academy API...</p>
                    <p>> Compiling study plan based on latest metrics...</p>
                    <p class="blink">_</p>
                </div>
            </div>
            <div class="agent-card">
                <div class="agent-icon pulsing-purple">⚙️</div>
                <h3>Evaluator Agent</h3>
                <p>Status: <span class="status-idle">Idle / Ready</span></p>
                <div class="agent-log">
                    <p>> Awaiting new submissions...</p>
                    <p>> Plagiarism scanner: Online</p>
                </div>
            </div>
            <div class="agent-card">
                <div class="agent-icon pulsing-green">📡</div>
                <h3>Coordinator Agent</h3>
                <p>Status: <span class="status-active">Active</span></p>
                <div class="agent-log">
                    <p>> Synchronizing team schedules...</p>
                    <p>> Generating metric reports...</p>
                </div>
            </div>
        </div>
        <div class="edubot-chat-wrapper" style="margin-top: 30px;">
            <div id="edubot-chat-window" class="chat-messages">
                <div class="chat-message bot">
                    <div class="msg-content">System initialized. Awaiting manual override or direct inquiry.</div>
                </div>
            </div>
            <form id="edubot-input-form" onsubmit="sendEduBotMessage(event)" class="chat-form">
                <div class="chat-input-container">
                    <input type="text" id="edubot-user-input" placeholder="Enter manual directive..." autocomplete="off">
                    <button type="submit" class="chat-send-btn">Send Directive</button>
                </div>
            </form>
        </div>
    </main>
    '''

    # Replace old edubot panel with new one
    import re
    # We will try to find <main id="edubot-panel"...</main> and replace it
    # If not found, we'll just append it to the end before </main> or something
    # Actually, EduBot panel might just be a div. Let's find it.
    match = re.search(r'<main id="edubot-panel".*?</main>', content, flags=re.DOTALL)
    if match:
        content = content[:match.start()] + agent_hub_html + content[match.end():]
    else:
        # If it wasn't found, maybe the id is different. Let's look for "EduBot Hesabatı" or "Agent Hub Report"
        match = re.search(r'<div id="edubot-panel".*?</div>', content, flags=re.DOTALL)
        if match:
             content = content[:match.start()] + agent_hub_html + content[match.end():]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_and_inject('index.html')
print("Index.html fixed")

def fix_script(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix broken function names in JS if any
    content = content.replace('showAgent HubPanel', 'showEduBotPanel')
    content = content.replace('nav-Agent Hub', 'nav-edubot')
    content = content.replace('Agent Hub Report', 'Agent Hub Telemetry')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_script('script.js')
print("script.js fixed")
