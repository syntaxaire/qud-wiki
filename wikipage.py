"""Class to assist with managing individual wiki articles on the Caves of Qud wiki."""

import re

from mwclient import Site

from config import config
from wiki_config import site, wiki_config

CREATED_SUMMARY = f'Created by {wiki_config["operator"]} using {config["Wiki name"]} {config["Version"]}'
EDITED_SUMMARY = f'Updated by {wiki_config["operator"]} using {config["Wiki name"]} {config["Version"]}'
PRE_TEMPLATE = "<!-- begin autogenerated section (please leave this marker) -->\n"
POST_TEMPLATE = "<!-- end autogenerated section (please leave this marker) -->\n"
# Link to work on or update regex:
# https://regex101.com/r/7ARrVM/5
# 1st matching group: the pre-template comment marker line
# 2nd matching group: Everything between the comment lines
# 3rd matching group: the word after the opening {{, for example, 'Item'
# 4th matching group: the word after the closing [[Category:, for example, 'Items'
# 5th matching group: the post-template comment marker line
TEMPLATE_RE = r"(?:.*)(<!-- begin autogenerated section \(please leave this marker\) -->\n)({{(\w*).*\n\[\[Category:(.*)]])\n(?:.*)(<!-- end autogenerated section \(please leave this marker\) -->\n*)(?:.*)"


class WikiPage:
    """Represent an individual article."""
    def __init__(self, qud_object):
        """Load the Caves of Qud wiki page for the given Qud object."""
        # is this page name overridden?
        if qud_object.name in config['Wiki']['Article overrides']:
            article_name = config['Wiki']['Article overrides'][qud_object.name]
        else:
            article_name = qud_object.displayname
        # capitalize first character
        self.blacklisted = False  # whether we will refuse all wiki work for this item
        if '[' in article_name or len(article_name) == 0:
            # mostly base categories that aren't listed as such, or objects that aren't meant
            # to be rendered (no display name)
            self.blacklisted = True
        else:
            self.article_name = article_name[0].upper() + article_name[1:]
            self.template_text = qud_object.wiki_template()
            self.page = site.pages[article_name]

    def exists(self):
        """Whether this page exists already."""
        return self.page.exists

    def upload_template(self):
        """Write the template for our object into the article and save it."""
        if self.exists():
            # complex case: have to get text indices corresponding to beginning of pre-template,
            # and end of post-template
            match = re.fullmatch(TEMPLATE_RE, self.page.text(), re.MULTILINE | re.DOTALL)
            pre_start = match.start(0)  # first character of PRE_TEMPLATE
            post_end = match.end(4)  # final character of POST_TEMPLATE
            pre_template_text = self.page.text()[:pre_start]
            post_template_text = self.page.text()[post_end:]
            new_text = pre_template_text + PRE_TEMPLATE + self.template_text + POST_TEMPLATE \
                + post_template_text
            self.page.save(text=new_text, summary=EDITED_SUMMARY)
        else:
            # simple case, creating an article
            text = PRE_TEMPLATE + self.template_text + POST_TEMPLATE
            self.page.save(text=text, summary=CREATED_SUMMARY)

    def infobox(self):
        """Retrieve the info template from the current page.
        Returns a tuple containing the text between the begin and end markers,
                                   the name of the template used,
                                   and the category applied."""
        match = re.search(TEMPLATE_RE, self.page.text(), re.MULTILINE | re.DOTALL)
        if not match:
            raise ValueError("No standard infobox in page, or no begin and end markers")
        return match[2], match[3], match[4]
