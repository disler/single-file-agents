prompt="$1"

# first shot
aider \
    --model o3-mini \
    --architect \
    --reasoning-effort high \
    --editor-model sonnet \
    --no-detect-urls \
    --no-auto-commit \
    --yes-always \
    --file *.py \
    --message "$prompt"

# reflection
aider \
    --model o3-mini \
    --architect \
    --reasoning-effort high \
    --editor-model sonnet \
    --no-detect-urls \
    --no-auto-commit \
    --yes-always \
    --file *.py \
    --message "Double check all changes requested to make sure they've been implemented: $prompt"
