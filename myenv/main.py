print("welcome to the movies app")
print("this is cool"
      "we will dot it "
      "this is cool"
      )

print("this is cool" "\n we will dot it" "\nthis is cool" )

print(
    """
this is cool
we will do it
this is cool
"""
)

followers = 10_000
name = "manju"

print(
    f"""
Hi,this is {name}.
I have {followers} followers
"""
)

def to_upper_case(text):
    """
    This helps in converting the text into uppercase
    """
    return text.upper() + "🥳"

print(to_upper_case(name))
print(help(to_upper_case))