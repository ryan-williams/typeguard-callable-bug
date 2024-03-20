import typeguard

# Example `typeguard_ignore` wrapper. In real code we'd conditionally override this with a no-op function, to avoid
# runtime overhead. However, even a trivial wrapper like this breaks the intended behavior of `typeguard_ignore`.
# typeguard_ignore = typeguard.typeguard_ignore


def typeguard_ignore(f):
    return typeguard.typeguard_ignore(f)
