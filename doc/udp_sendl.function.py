
fxs.append(
    {
        "name": "udp_sendl",
        "info": "sends an UDP packet",
        "result": {
            "type": "int",
            "success": "0",
            "error": "-1",
        },
        "args": [
           {
               "name": "s",
               "type": "int",
               "info": "Handle of the UDP socket.",
           },
           {
               "name": "addr",
               "type": "const struct ipaddr*",
               "dill": True,
               "info": "IP address to send the packet to. If set to **NULL** " +
                     "remote address specified in **udp_open** function will " +
                     "be used.",
           },
        ],
        "protocol": udp_protocol,
        "prologue": """
            This function sends an UDP packet.

            Given that UDP protocol is unreliable the function has no deadline.
            If packet cannot be sent it will be silently dropped.
        """,

        "has_handle_argument": True,
        "has_iol": True,

        "errors": ["EINVAL", "EMSGSIZE"],
        "custom_errors": {
            "EMSGSIZE": "The message is too long to fit into an UDP packet.",
        }
    }
)