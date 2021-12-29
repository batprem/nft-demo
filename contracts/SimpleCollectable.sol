// SPDX-License-Identifier: MIT


pragma solidity 0.6.6;


import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";


contract SimpleCollectable is ERC721{
    uint256 public tokenCounter = 0;
    constructor() public ERC721 ("Dogie", "DOG"){
        
    }

    function createCollectable(string memory tokenURI) public returns  (uint256) {
        // Assign TokenId to the new owner
        // _safeMint funcation protect NFT replacement
        uint256 newTokenId = tokenCounter;
        _safeMint(
            msg.sender, // Address of who calls this function
            newTokenId // Token 0, 1, 2, ....
        );
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter++;
        return newTokenId;
    }
    // Token URI is resource identify like http or ipfs or any url
}