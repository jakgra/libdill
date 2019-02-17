
newFunction(
    {
        name: "tcp_listener_fromfd",
        info: "wraps an existing OS-level file descriptor",

        result: {
            type: "int",
            success: "newly created socket handle",
            error: "-1",
        },
        args: [
            {
                name: "fd",
                type: "int",
                info: "File descriptor of a listening TCP socket to wrap.",
            },
        ],

        protocol: tcp_protocol,

        prologue: `
            This function wraps an existing OS-level file descriptor.
        `,
        epilogue: `
            The socket can be cleanly shut down using **tcp_close** function
            which will also close the underlying file descriptor.

            There's no way to unwrap the file descriptor.
        `,

        allocates_handle: true,
        mem: "tcp_listener_storage",

        example: `
            int fd = socket(AF_INET, SOCK_STREAM, 0);
            bind(fd, addr, sizeof(addr));
            listen(fd, 10);
            int s = tcp_listener_fromfd(fd);
        `
    }
)
