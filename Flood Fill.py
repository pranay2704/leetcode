def floodFill(image, sr, sc, color):
    # Capture the original color of the starting pixel
    oldColor = image[sr][sc]
    
    # If the starting pixel is already the target color, return the image
    if oldColor == color:
        return image
    
    rows, cols = len(image), len(image[0])
    
    def dfs(r, c):
        # Base case: check boundaries and if pixel matches the original color
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != oldColor:
            return
        
        # Update the pixel color
        image[r][c] = color
        
        # Recurse for all 4-directionally adjacent pixels
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    dfs(sr, sc)
    return image
