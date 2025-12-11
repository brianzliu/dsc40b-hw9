def learn_theta(data, colors):
    max_blue = float('-inf')
    min_red = float('inf')
    
    for i in range(len(data)):
        value = data[i]
        color = colors[i]
        
        if color == 'blue':
            if value > max_blue:
                max_blue = value
        elif color == 'red':
            if value < min_red:
                min_red = value
                
    theta = (max_blue + min_red) / 2.0
    
    return theta

def compute_ell(data, colors, theta):
    loss = 0
    for i in range(len(data)):
        val = data[i]
        col = colors[i]
        
        if col == 'red' and val <= theta:
            loss += 1
        elif col == 'blue' and val > theta:
            loss += 1
            
    return float(loss)

def minimize_ell(data, colors):
    best_theta = 0.0
    min_loss = float('inf')
    
    for x in data:
        current_loss = compute_ell(data, colors, x)
        
        if current_loss < min_loss:
            min_loss = current_loss
            best_theta = x
            
    return best_theta

def minimize_ell_sorted(data, colors):
    total_blues = 0
    for c in colors:
        if c == 'blue':
            total_blues += 1
            
    red_count = 0 
    blue_count = 0 
    
    min_loss = total_blues
    best_theta = data[0] - 1.0 
    
    for i in range(len(data)):
        val = data[i]
        col = colors[i]
        
        if col == 'red':
            red_count += 1
        else:
            blue_count += 1

        current_loss = red_count + (total_blues - blue_count)
        
        if current_loss < min_loss:
            min_loss = current_loss
            best_theta = val
            
    return best_theta