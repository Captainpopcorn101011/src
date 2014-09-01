CFSpeech       = 1 << 0
CFThought      = 1 << 1
CFQuicktalker  = 1 << 2
CFTimeout      = 1 << 3
CFPageButton   = 1 << 4
CFQuitButton   = 1 << 5
CFNoQuitButton = 1 << 6
CFReversed     = 1 << 7

WTNormal = 0
WTQuickTalker = 1
WTSystem = 2
WTBattleSOS = 3
WTEmote = 4
WTToontownBoardingGroup = 5

# Foreground, background:
WhisperColors = {
    WTNormal: (
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.6, 0.8, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.9, 0.6)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.8, 0.6))   # Disabled
    ),
    WTQuickTalker: (
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.6, 0.8, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.9, 0.6)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.8, 0.6))   # Disabled
    ),
    WTSystem: (
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.4, 1.0, 0.8)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6))   # Disabled
    ),
    # TODO: WTBattleSOS
    WTEmote: (
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.5, 0.1, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.2, 0.6)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.1, 0.6))   # Disabled
    )
    # TODO: WTToontownBoardingGroup
}
