import { useEffect, useState } from "react";
import { get, post } from '@/lib/ft_axios';
import { Swords, UserPlus } from "lucide-react";
import { Button } from "@/components/ui/button";
import { toast } from "react-toastify";

export default function InviteButton({ user_id, type, defaultStatus, ...props }) {

    console.log(user_id);
    
    const [status, setStatus] = useState(defaultStatus);


    useEffect(() => {
        const fetchStatus = async () => {
            try {
                console.log("tsiftat req");
                
                const response = await get(`/invitation-status/${type}/${user_id}`);
                console.log("invite button", response);
                if (response.status === "blocked") {
                    setStatus("Unblock User");
                } else {
                    setStatus(`${type} Invite ${response.status}`);
                }
            } catch (e) {
                if (e.response && e.response.status === 404) {
                    setStatus(defaultStatus);
                }
                console.log(e);
            }
        }

        fetchStatus();
    }, [user_id])

    const sendInvite = async (target) => {
        try {
            if (status === "Unblock User") {
                await post('/deblockFriend/', {
                    "user1": target,
                    "type": "friend"
                });
                setStatus(`${type} Invite Accepted`); // type will be capitalized by tailwind classname
            } else {
                await post('/invite/', {
                    "user1": target,
                    "type": type
                });
                setStatus(`${type} Invite Pending`); // type will be capitalized by tailwind classname
            }

            toast.success(type.charAt(0).toUpperCase() + type.slice(1) + " request sent successfully!");
        } catch (e) {
            console.log(e);
            toast.error("Failed to send " + type + " request. Please try again.");
        }

    }


    return (
        <Button onClick={() => sendInvite(user_id)} variant="outline" {...props} disabled={status !== defaultStatus && status !== "Unblock User"}>
            {type === "game" ? <Swords /> : <UserPlus />} {defaultStatus === "" ? "" : status}
        </Button>
    )
}