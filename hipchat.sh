#!/bin/bash

# Set the ROOM_ID & AUTH_TOKEN variables below.
# Further instructions at https://www.hipchat.com/docs/apiv2/auth

ROOM_ID=881    #881
AUTH_TOKEN=XOKRm6zyEigL4JJ7c5WDj3ZXfFfrBdv3DRrWt2ka
MESSAGE="Hello world!, fucking world, please help me"

curl -H "Content-Type: application/json" \
     -X POST \
     -d "{\"color\": \"purple\", \"message_format\": \"text\", \"message\": \"$MESSAGE\" }" \
     https://chat.hipchat.com/v2/room/$ROOM_ID/notification?auth_token=$AUTH_TOKEN

