function SetupRedmi
{
  CARD_NUM=$(aplay -l | grep Redmi | sed -n 's/^card \([0-9][0-9]*\):.*/\1/p')
  echo "CARD_NUM=$CARD_NUM"
  amixer -c $CARD_NUM set PCM 100% unmute

  # CARD_NUM=$(pactl list short sinks | grep Redmi | sed -n 's/^\([0-9][0-9]*\)[ \t].*/\1/p')
  # echo "CARD_NUM=$CARD_NUM"
  # pactl set-default-sink $CARD_NUM
  # pactl set-sink-volume $CARD_NUM 100%
  # pactl set-sink-mute $CARD_NUM 0
}
