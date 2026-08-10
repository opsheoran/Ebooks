import re
from bs4 import BeautifulSoup, NavigableString

eng = """<div class="body">
<p>There are mainly four types of frequency curves:</p>
<ol>
<li>
<p><strong>Symmetrical Frequency Curve:</strong> This curve is bell-shaped and perfectly symmetrical around its center. The mean, median, and mode all lie at the center point. Example: Normal distribution curve.</p>
[[VISUAL_BLOCK_0]]</li>
<li>
<p><strong>Moderately Asymmetrical (Skewed) Frequency Curve:</strong> This curve is not symmetrical. It has a longer tail on one side.</p>
<ul>
<li><strong>Positively Skewed:</strong> The longer tail extends to the right (towards higher values). Here, Mean > Median > Mode.</li>
<li><strong>Negatively Skewed:</strong> The longer tail extends to the left (towards lower values). Here, Mean < Median < Mode.</li>
</ul>
[[VISUAL_BLOCK_1]]</li>
<li>
<p><strong>J-shaped Frequency Curve:</strong> This curve shows maximum frequency at one extreme end of the distribution. It looks like the letter 'J' (or a reverse 'J'). Example: Wealth distribution, where most people have low wealth and very few have high wealth.</p>
[[VISUAL_BLOCK_2]]</li>
<li>
<p><strong>U-shaped Frequency Curve:</strong> This curve shows maximum frequencies at both extreme ends and minimum frequency in the middle. Example: Cloudiness frequency, where days are either very clear or very cloudy, but rarely in between.</p>
[[VISUAL_BLOCK_3]]</li>
</ol>
</div>"""

eng_parts = re.split(r'(\[\[VISUAL_BLOCK_\d+\]\])', eng)
print(len(eng_parts))
