# judgment, response
# Yx = sum(Bx,j)(Xj) + errorx
# predicted user response
# Zx = sum(Bx,j)(Xj)
# user weights
# Bx
# response linearity
# Rx = P (Yx, Zx)
# environment
# Ye = sum(Be,j)(Xj) + errore
# environment weights
# Be
# predicted environmental criterion
# Ze = sum(Be,j)(Xj)
# environmental predictability
# Re = P (Ye, Ze)
# achievement index
# Ra = P(Yx,Ye)
# matching index - G
# how well functions and weights of Z are represented in X
# G = P(Zx,Ze)
# Ra = G*Re*Rx
# Error correlation
# if C = 0 (independent), otherwise variable omission or cues used in a non-linear manner
# high C may mean accuracy in cue linear use, configural use or nonlinear use or unmodelled knowledge
# onlinearity refers to nonlinear transformations before combination
# configuration means interactions between cues (dependence)
# C = P(errorx,errore)
# GRx = performance, match requirements and consistent
# GRe = validity of model




class Instance:
    def __init__(self, cue, environment):
        self.cues = np.array(cue)
        self.environments = np.array(environment)

class Brunswick:
    def __init__(self, n_input, n_output):

class cueState:
    def __init__(self,action):
        self.action = action

class environmentState:
    def __init__(self,action):
        self.action = action

cueState.gone = cueState("1")
cueState.remote
cueState.distal
cueState.proximal
cueState.peripheral
cueState.central

environmentState.gone = cueState("1")
environmentState.remote
environmentState.distal
environmentState.proximal
environmentState.peripheral
environmentState.central

class achievementScore:
    def __init__(self,action):
    self.action = action


#Bs,j
class userWeights:
    def __init__(self,action):
    self.action = action

#
class environmentWeights:
    def __init__(self,action):
    self.action = action
