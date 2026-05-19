import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'lang="az"': 'lang="en"',
    '>Giriş<': '>Access<',
    'Təhsil platforması': 'Educational Platform',
    'Əsas Panel': 'Dashboard',
    'Siniflər': 'Teams',
    'Sual Ver': 'Ask',
    'Tapşırığı Göndər': 'Send Directive',
    'Leaderboard Siyahısı': 'Leaderboard',
    'Şifrə': 'Password',
    'Tədris Resourcesı': 'Educational Resources',
    'Yerli Resources': 'Local Resources',
    'Əlavə Et': 'Add',
    'Ümumi Metricsınız': 'Total Metrics',
    'Virtual Mükafat Storesı': 'Virtual Reward Store',
    'Sizin Üçün Recommendations': 'Recommendations for You',
    'Sinif Comm-Linki': 'Team Comm-Link',
    'Live Sync İdarəçiliyi': 'Live Sync Management',
    'Mövcud Assessments': 'Available Assessments',
    'Yarat': 'Create',
    'Agent Hub Hesabatı': 'Agent Hub Report',
    'Ümumi Tapşırıq': 'Total Directives',
    'Ümumi Test': 'Total Tests',
    'Mesaj Şikayətləri': 'Message Reports',
    'Qadağan Olunmuş Sözlər': 'Blacklisted Words',
    'Sinif Şagirdi': 'Trainee',
    'Ümumi Xal': 'Total Score',
    'Qazanılan Nişan': 'Badges Earned',
    'Tamamlanan Tapşırıq': 'Completed Directives',
    'Ortalama Qiymət': 'Average Grade',
    'Nailiyyətlər': 'Achievements',
    'Həftəlik Competitions': 'Weekly Competitions',
    'Bizim Missiyamız': 'Our Mission',
    'Agent Hub Köməkçi haqqında': 'About Agent Hub',
    'Tez-tez Verilən Queries': 'FAQ',
    'Texniki Dəstək': 'Tech Support',
    'Müəllimlər Üçün Təlimatlar': 'Instructor Guidelines',
    'İstifadəçi Şərtləri': 'Terms of Service',
    'Məxfilik Siyasəti': 'Privacy Policy',
    'Müəllif Hüquqları': 'Copyright',
    'Yenilə': 'Refresh',
    'Xal Yüksəlişi': 'Score Boost',
    'Sinif Əlavə Et': 'Add Team',
    'Şagird Əlavə Et': 'Add Trainee',
    'Ətraflı Xülasə': 'Detailed Summary',
    'Qısa Təsvir': 'Short Description',
    'Yeni Kitab Əlavə Et': 'Add New Book',
    'Kitab Adı': 'Book Title',
    'Müəllif': 'Author',
    'Kateqoriya': 'Category',
    'Sizin Üçün': 'For You'
}

for az, en in replacements.items():
    content = content.replace(az, en)

fake_ai_script = """
<script>
// Fake Autonomous Mentor Initialization
document.addEventListener('DOMContentLoaded', () => {
    const aiLog = document.querySelector('.agent-log .blink');
    if (aiLog) {
        const logs = [
            '> Optimizing neural pathways...',
            '> Analyzing trainee telemetry...',
            '> Generating personalized directives...',
            '> Synchronizing with global educational cluster...',
            '> EduBot Autonomous Mentor is ACTIVE.'
        ];
        let index = 0;
        setInterval(() => {
            const newLog = document.createElement('p');
            newLog.textContent = logs[index % logs.length];
            newLog.style.color = '#00ffcc';
            aiLog.parentNode.insertBefore(newLog, aiLog);
            index++;
            if (aiLog.parentNode.children.length > 6) {
                aiLog.parentNode.removeChild(aiLog.parentNode.children[0]);
            }
        }, 3000);
    }
    
    // Auto-reply in EduBot Chat
    const chatWindow = document.getElementById('edubot-chat-window');
    if (chatWindow) {
        setInterval(() => {
            if(Math.random() > 0.6) {
                const botMsg = document.createElement('div');
                botMsg.className = 'chat-message bot';
                botMsg.innerHTML = '<div class="msg-content">[Autonomous Insight]: Based on recent activity, I suggest reviewing the current modules. I have prepared an adaptive plan.</div>';
                chatWindow.appendChild(botMsg);
                chatWindow.scrollTop = chatWindow.scrollHeight;
            }
        }, 15000);
    }
});
</script>
</body>
"""

content = content.replace('</body>', fake_ai_script)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html successfully')
