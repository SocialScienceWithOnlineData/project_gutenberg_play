"""
project_gutenberg_play provides helper functions for exploring project gutenberg texts.
"""
import re
import pprint
import urllib.request   # another import that you've seen. This lets us search the internet.  
                        #You plug in a url and you'll get any page back.
def gutenbergURLToText( url ):
  # Pull text from project gutenberg
  response = urllib.request.urlopen(url)
  works_raw = response.read().decode('utf-8') # this gets the raw text of the book back in a way that it's easy to work with.
  return( works_raw )

def gutenbergTextToList( rawtext ): 
  works_texts = []  

  for line in rawtext.split("\r\n"): # This \r\n business is a code for what the Enter key creates to make new lines.  
                                       # What we're doing is reading the text one line at time
    line = line.strip(" :")   # helps catching of titles in text, which use space inconsistently
    if line == "THE SONNETS": # Don't start reading until after the boilerplate frontmatter 
      works_texts = []  
    if line == "*** END OF THE PROJECT GUTENBERG EBOOK THE COMPLETE WORKS OF WILLIAM SHAKESPEARE ***": # Stop reading before the boilerplate endmatter
      break
    # now lets start putting text we find into the list
    # Break text into a list. From each word remove internal and outside punctuation
    line = re.sub(r',|_|—', " ", line)
    line = [ word.strip(",’:;.'()?! ") for word in line.split() ]
    line = [ word for word in line if len( word ) > 0 ]
    # We've turned each work into a list of words. Then we can easily see which words are in the list.
    works_texts.extend( line ) # this adds the words in a line to the growing works.
  return( works_texts )

def gutenbergURLToList( url ):
  rawtext = gutenbergURLToText( url )
  listtext = gutenbergTextToList( rawtext )
  return( listtext )

def palindrome( string ):
  return( string == string[::-1] )
