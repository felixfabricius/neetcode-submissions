"""
Approach:
- Can compare word i and word i + 1, and 
  if word i is a prefix of word i + 1 and len(word i) < len(word i + 1):
    - we learn nothing about order
    - we need to keep track of unique letters
  if word i + 1 is a prefix of word i and len(word i + 1) < len(word i):
    - return ""
  else: compare character by character. the first times characters differ
  add adj_list[char in word i].add(adj_list[char in word i + 1])
  I.e. directed edge in graph represents < relation in lexicographical ordering

- At the end:
  - we have a valid lexicographical ordering if we didn't return anything early and there are no cycles in our graph
    to check this:
    - somehow need to find the 'roots' of our graph, i.e. the vertices which have no edges pointing towards them, but
      from which edges are pointing
      what if we built our adj_list to store both descendants of a node and also parents? then we can traverse both ways.
    given: set of nodes which either have edges pointing to them, or from them; and all the relevant edges
    "no cycles" means:
    - follow all possible "directional" paths from one such node (i.e. one path just in one direction; and another path just in another)
      keep track of nodes that we've seen. must not get any duplicates this way
      That's not quite true. Imagine e.g. diamond shape, and starting from bottom.
      Rather: must not get any overlap between sets of nodes we reach from paths in one direction, and set we reach from another direction I think.
      Yeah, that's kind of the definition of a cycle.
    

    But: there might still be nodes left that we haven't reached this way.
    If we repeat this exercise from a node that we haven't yet seen, resetting the "currently seen" nodes, will we eventually reach all the nodes?
    Is it true that once we choose a new focal node, we should reset our set of currently seen nodes?
    I think so, yes. 
  - how to deal with nodes which have no edges pointing towards them but also no edges pointing away?
    those can be inserted anywhere, in any order
    can perhaps keep track of them somewhere

    Is it possible that we see all the nodes this way, but might miss an edge between nodes that we've already seen?
    Yes, that is possible.
    But: maybe if we miss such an edge, that means that that edge is not part of a cycle? (this is actually really difficult.)

    Can ensure that we traverse all the edges by creating a set of:
    - nodes that have edges pointing from
    - nodes that have edges pointing to

    Note that a cycle can only exist among nodes that have both edges pointing from and edges pointing to!
    So can simply take the intersection of these two sets, and check for cycles just for the subgraph induced by those vertices.
    
    Would our above problem then still be possible?
    - Can avoid by literatlly doing this traversal thing from every possible node!
    - More efficient approach?
      - 
    
    Possible alternative approach:
    - Let's look at our adjacency list.
    - Cycles in graph can include only vertices which have edges pointing to and from them.
      They will also only involve edges that are connected to those vertices.
      Therefore, we can remove all other vertices AND any edge that involves any other vertex.
      This provides a subgraph.
    - Once we removed some vertices and edges, we might now have new vertices and edges that 
      only have edges pointing into at most one direction attached to them.
    - So we can repeat this process.
    - If there are no cycles contained in our graph, then eventually we should be able to remove ALL
      vertices and edges this way.
    - Note that this iterative approach would also allow us to specify a valid ordering.
      At each iteration, the vertices we remove which have only children get appended to the start of our string.
      And the vertices we remove which have only parents, get appended to the end.
      Vertices which have neither children nor parents can get attached to either substring.
      At the end, we can concatenate our "start" and our "end" substrings.
    
    Complexity of this approach:
    - Build the adjacency lists:
      - Time: O(total number of characters) + O(unique characters?)

    - At each iteration:
      - Identify vertices which have only edges in one direction attached to them. O(V) each iteration (can do O(1) checks of set size)
      - Add those vertices to "start" or "end" substring. O(V) across all the iterations.
      - Remove those vertices. O(V) across all the iterations.
      - For other vertices, remove the edges pointing to these vertices. Since we have bidirectional edges recorded,
        this is simply O(E) across all the iterations.   
"""

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Build adjacency list
        # Compare all the words pairwise and keep track of unique characters
        graph = {}
        for i, word in enumerate(words):
            # If it's the last word, then simply add unique characters if this hasn't happened yet
            # No need to check for edges.
            # This will only do anything, if there is only 1 word in total
            if i == len(words) - 1:
                for char in word:
                    if char not in graph:
                        graph[char] = [set(), set()]
                continue
            # Else: compare with following word
            next_word = words[i + 1]
            # Iterate through all the characters in the words until: characters don't match, or one word ended
                # If characters match: simply append them to our graph
                # Else if there is a mismatch: append characters and edges to graph
                # If there is no match until the end of the comparisons, check if order is at all possible!
                
                # Regardless of whether there was mismatch or not, need to add remaining characters in word(s) 
                # to our graph. So can keep track of character position of the last characters that we added,
                # and then add any ensuing characters to our graph as vertices.
            mismatch = False
            j = 0
            while not mismatch and j < min(len(word), len(next_word)):
                if word[j] == next_word[j]:
                    if word[j] not in graph:
                        graph[word[j]] = [set(), set()]
                else:
                    mismatch = True
                    # First part of this graph points to children, which come after in lexicographic ordering
                    # CAREFULL: .add() returns None and modifies in place. Rather: need to do union.
                    # So this does not work:
                      # graph[word[j]] = graph.get(word[j], [set(), set()])[0].add(next_word[j])
                    if not word[j] in graph:
                      graph[word[j]] = [{next_word[j]}, set()]
                    else:
                      graph[word[j]][0].add(next_word[j])
                    if not next_word[j] in graph:
                      graph[next_word[j]] = [set(), {word[j]}]
                    else:
                      graph[next_word[j]][1].add(word[j])
                j += 1

            # If mismatch is False, check if lenghts match adequately.
            if not mismatch:
                if len(word) > len(next_word):
                  # Strict inequality because can have duplicate words
                    return ""

            # Add remaining characters
            for k in range(j, len(word)):
                if word[j] not in graph:
                    graph[word[j]] = [set(), set()]

            for k in range(j, len(next_word)):
                if next_word[j] not in graph:
                    graph[next_word[j]] = [set(), set()]
        print(graph)
        # Iteratively remove vertices and edges from adjaceny list
        start = ""
        end = ""
        cycle_detected = False
        while len(graph) > 0 and not cycle_detected:
          # If there is no vertex in subgraph that either has only edges pointing to
          # or only edges pointing from, then we have a cycle
          cycle_detected = True
          # Scan through each vertex
          for char in list(graph.keys()):
            print(f"char: {char}")
            if len(graph[char][0]) == 0:
              cycle_detected = False
              # no edges pointing from the character, so no remaining after char in ordering
              end = char + end
              # Remove all the edges
              for other_char in graph[char][1]:
                graph[other_char][0].remove(char)
              # Remove the character from the graph
              del graph[char]
            elif len(graph[char][1]) == 0:
              cycle_detected = False
              # no edges pointing to the character, so no remaining character is before the character
              # in the ordering
              start = start + char
              for other_char in graph[char][0]:
                print(f"  other_char: {other_char}")
                print(f"  graph[other_char]: {graph[other_char]}")
                graph[other_char][1].remove(char)
              del graph[char]
              
            # Note that characters without any edges pointing either to or from can be added wherever

        return "" if cycle_detected else start + end